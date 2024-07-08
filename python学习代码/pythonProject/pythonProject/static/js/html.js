const minValue = Math.min(...values);
const maxValue = Math.max(...values);

const chartConfig = {
    type: type,
    data: {
        labels: labels,
        datasets: [{
            label: document.getElementById("modalTitle").textContent,
            data: values,
            backgroundColor: type === 'pie' ? values.map(() => `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 0.6)`) : 'rgba(75, 192, 192, 0.6)',
            borderColor: 'rgba(75, 192, 192, 1)',
            fill: type === 'line' ? false : true
        }]
    },
    options: {
        scales: {
            x: {
                title: {
                    display: true,
                    text: '序号'
                }
            },
            y: {
                min: minValue - (maxValue - minValue) * 0.1,
                max: maxValue + (maxValue - minValue) * 0.1,
                title: {
                    display: true,
                    text: '数值'
                }
            }
        },
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            }
        }
    }
};
