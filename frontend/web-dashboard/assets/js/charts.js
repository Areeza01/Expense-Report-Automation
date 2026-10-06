let expenseChart = null;

function renderChart() {
    const canvas = document.getElementById("expenseChart");

    if (!canvas) {
        console.warn("expenseChart canvas not found.");
        return;
    }

    if (typeof Chart === "undefined") {
        console.error("Chart.js is not loaded.");
        return;
    }

    // Destroy the previous chart if it exists
    if (expenseChart) {
        expenseChart.destroy();
    }

    expenseChart = new Chart(canvas, {
        type: "pie",

        data: {
            labels: [
                "Meals",
                "Travel",
                "Accommodation",
                "Equipment"
            ],

            datasets: [
                {
                    label: "Expenses",
                    data: [
                        10,
                        8,
                        4,
                        3
                    ],

                    backgroundColor: [
                        "#7C3AED",
                        "#EC4899",
                        "#3B82F6",
                        "#10B981"
                    ],

                    borderWidth: 2,
                    borderColor: "#ffffff"
                }
            ]
        },

        options: {
            responsive: true,

            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
}