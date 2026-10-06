/*
=========================================
SECTION LOADER
=========================================
*/

async function loadSection(section) {

    try {

        const response = await fetch(
            `sections/${section}.html`
        );

        if (!response.ok) {
            throw new Error(
                `Unable to load ${section}`
            );
        }

        const html =
            await response.text();

        document.getElementById(
            "content"
        ).innerHTML = html;

        switch (section) {

            case "dashboard":
                loadDashboard();
                break;

            case "expenses":
                loadExpenses();
                break;

            case "approvals":
                loadApprovals();
                break;

            case "reports":
                loadReports();
                break;
        }

    } catch (error) {

        console.error(error);

        document.getElementById(
            "content"
        ).innerHTML = `
            <div class="card">
                <h2>Something went wrong</h2>
                <p>${error.message}</p>
            </div>
        `;
    }
}

/*
=========================================
DASHBOARD
=========================================
*/

async function loadDashboard() {

    try {

        const response = await fetch(
            `${API_URL}/expenses/`
        );

        const expenses =
            await response.json();

        let totalAmount = 0;
        let approved = 0;
        let pending = 0;

        let rows = "";

        expenses.forEach(expense => {

            totalAmount +=
                Number(expense.amount || 0);

            if (
                expense.status?.toLowerCase()
                === "approved"
            ) {
                approved++;
            }

            if (
                expense.status?.toLowerCase()
                === "pending"
            ) {
                pending++;
            }

            rows += `
                <tr>
                    <td>${expense.merchant}</td>
                    <td>$${expense.amount}</td>
                    <td>${expense.category}</td>
                    <td>${expense.status}</td>
                </tr>
            `;
        });

        if (
            document.getElementById(
                "totalExpenses"
            )
        ) {
            document.getElementById(
                "totalExpenses"
            ).textContent =
                expenses.length;
        }

        if (
            document.getElementById(
                "totalAmount"
            )
        ) {
            document.getElementById(
                "totalAmount"
            ).textContent =
                `$${totalAmount}`;
        }

        if (
            document.getElementById(
                "approvedCount"
            )
        ) {
            document.getElementById(
                "approvedCount"
            ).textContent =
                approved;
        }

        if (
            document.getElementById(
                "pendingCount"
            )
        ) {
            document.getElementById(
                "pendingCount"
            ).textContent =
                pending;
        }

    } catch(error) {

        console.error(
            "Dashboard Error:",
            error
        );

    }
}

/*
=========================================
UPLOAD RECEIPT
=========================================
*/

async function uploadReceipt() {

    const fileInput =
        document.getElementById(
            "receiptFile"
        );

    const result =
        document.getElementById(
            "uploadResult"
        );

    const file =
        fileInput?.files[0];

    if (!file) {

        result.innerHTML = `
            <p style="color:red">
                Please select a file.
            </p>
        `;

        return;
    }

    const formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    result.innerHTML =
        "Uploading...";

    try {

        const response =
            await fetch(
                `${API_URL}/receipts/upload`,
                {
                    method: "POST",
                    body: formData
                }
            );

        const data =
            await response.json();

        result.innerHTML = `

            <div class="card">

                <h2>
                    Receipt Processed
                </h2>

                <br>

                <p>
                    <strong>
                        Merchant:
                    </strong>

                    ${data.receipt_data?.merchant_name}
                </p>

                <p>
                    <strong>
                        Amount:
                    </strong>

                    $${data.receipt_data?.total_amount}
                </p>

                <p>
                    <strong>
                        Category:
                    </strong>

                    ${data.category?.category}
                </p>

                <p>
                    <strong>
                        Recommendation:
                    </strong>

                    ${data.approval?.recommendation}
                </p>

            </div>

        `;

    } catch(error) {

        console.error(error);

        result.innerHTML = `
            <p style="color:red">
                Upload failed
            </p>
        `;
    }
}

/*
=========================================
EXPENSES
=========================================
*/

async function loadExpenses() {

    try {

        const response =
            await fetch(
                `${API_URL}/expenses/`
            );

        const expenses =
            await response.json();

        const table =
            document.getElementById(
                "expenseTable"
            );

        if (!table) return;

        let rows = "";

        expenses.forEach(expense => {

            rows += `
                <tr>

                    <td>${expense.id}</td>

                    <td>${expense.merchant}</td>

                    <td>$${expense.amount}</td>

                    <td>${expense.category}</td>

                    <td>

                        <span
                            class="status-${expense.status.toLowerCase()}">

                            ${expense.status}

                        </span>

                    </td>

                    <td>

                        <button
                            class="approve-btn"
                            onclick="approveExpense(${expense.id})">

                            Approve

                        </button>

                        <button
                            class="reject-btn"
                            onclick="rejectExpense(${expense.id})">

                            Reject

                        </button>

                    </td>

                </tr>
            `;
        });

        table.innerHTML = rows;

    } catch(error) {

        console.error(
            "Expense Error:",
            error
        );

    }
}

/*
=========================================
APPROVE
=========================================
*/

async function approveExpense(id) {

    try {

        const response = await fetch(
            `${API_URL}/expenses/${id}/approve`,
            {
                method: "PUT"
            }
        );

        console.log(
            await response.json()
        );

        loadExpenses();

    } catch (error) {

        console.error(error);
    }
}

/*
=========================================
REJECT
=========================================
*/

async function rejectExpense(id) {

    try {

        const response = await fetch(
            `${API_URL}/expenses/${id}/reject`,
            {
                method: "PUT"
            }
        );

        console.log(
            await response.json()
        );

        loadExpenses();

    } catch (error) {

        console.error(error);
    }
}

/*
=========================================
APPROVALS PAGE
=========================================
*/

async function loadApprovals() {

    try {

        const response =
            await fetch(
                `${API_URL}/expenses/`
            );

        const expenses =
            await response.json();

        const table =
            document.getElementById(
                "approvalTable"
            );

        if (!table) return;

        const pending =
            expenses.filter(
                expense =>
                    expense.status
                    ?.toLowerCase() ===
                    "pending"
            );

        let rows = "";

        pending.forEach(expense => {

            rows += `
                <tr>

                    <td>${expense.id}</td>

                    <td>${expense.merchant}</td>

                    <td>

                        <span class="status-pending">

                            Pending

                        </span>

                    </td>

                </tr>
            `;
        });

        table.innerHTML = rows;

    } catch(error) {

        console.error(
            "Approvals Error:",
            error
        );

    }
}

/*
=========================================
REPORTS
=========================================
*/

async function loadReports() {

    try {

        const response =
            await fetch(
                `${API_URL}/expenses/`
            );

        const expenses =
            await response.json();

        const categories = {};

        expenses.forEach(expense => {

            const category =
                expense.category || "Other";

            categories[category] =
                (categories[category] || 0) + 1;
        });

        const canvas =
            document.getElementById(
                "expenseChart"
            );

        if (!canvas) return;

        new Chart(canvas, {

            type: "pie",

            data: {

                labels:
                    Object.keys(
                        categories
                    ),

                datasets: [

                    {
                        data:
                            Object.values(
                                categories
                            ),

                        backgroundColor: [

                            "#7C3AED",
                            "#EC4899",
                            "#10B981",
                            "#F59E0B",
                            "#3B82F6"

                        ]
                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false

            }

        });

    } catch(error) {

        console.error(
            "Reports Error:",
            error
        );
    }
}

/*
=========================================
GLOBAL FUNCTIONS
=========================================
*/

window.approveExpense =
    approveExpense;

window.rejectExpense =
    rejectExpense;

window.uploadReceipt =
    uploadReceipt;

/*
=========================================
START APP
=========================================
*/

window.onload = () => {

    console.log(
        "ExpenseFlow Loaded"
    );

    loadSection(
        "dashboard"
    );

};

window.approveExpense = approveExpense;
window.rejectExpense = rejectExpense;
window.uploadReceipt = uploadReceipt;