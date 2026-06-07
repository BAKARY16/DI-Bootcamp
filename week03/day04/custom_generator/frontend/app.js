function $id(id) {
    return document.getElementById(id);
}

function setActiveTab(tabName) {
    document.querySelectorAll('nav button').forEach(button => {
        button.classList.toggle('active', button.dataset.tab === tabName);
    });
    document.querySelectorAll('.tab').forEach(section => {
        section.classList.toggle('active', section.id === tabName);
    });
}

document.querySelectorAll('nav button').forEach(button => {
    button.addEventListener('click', () => setActiveTab(button.dataset.tab));
});

function buildChart(canvasId, type, labels, values, label, color) {
    const canvasElement = document.getElementById(canvasId);
    if (!canvasElement) {
        console.warn(`Canvas ${canvasId} non trouvé`);
        return;
    }
    const ctx = canvasElement.getContext('2d');
    
    return new Chart(ctx, {
        type,
        data: {
            labels: labels || [],
            datasets: [{
                label: label || 'Données',
                data: values || [],
                backgroundColor: color,
                borderColor: '#1f2937',
                borderWidth: 1,
                fill: type === 'line' ? false : true,
                tension: 0.35,
                pointRadius: type === 'line' ? 4 : 0,
                pointBackgroundColor: color,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: { 
                    mode: 'index', 
                    intersect: false,
                    backgroundColor: 'rgba(0,0,0,0.8)',
                    padding: 10,
                    cornerRadius: 6,
                }
            },
            scales: {
                y: { 
                    beginAtZero: true,
                    ticks: { font: { size: 12 } },
                    grid: { color: '#f0f0f0' }
                },
                x: { 
                    ticks: { 
                        autoSkip: true, 
                        maxRotation: 45,
                        minRotation: 0,
                        font: { size: 12 }
                    },
                    grid: { display: false }
                }
            }
        }
    });
}

fetch('data.json')
    .then(response => response.json())
    .then(data => {
        $id('user-count').textContent = data.summary.users;
        $id('activity-count').textContent = data.summary.total_activities;
        $id('chi2-value').textContent = data.summary.chi2.toFixed(2);
        $id('p-value').textContent = data.summary.p_value.toFixed(4);

        const topInterests = $id('top-interests');
        data.top_interests.forEach(([interest, count]) => {
            const li = document.createElement('li');
            li.textContent = `${interest} : ${count}`;
            topInterests.appendChild(li);
        });

        const topHours = $id('top-hours');
        data.top_hours.forEach(([hour, count]) => {
            const li = document.createElement('li');
            li.textContent = `Heure ${hour}h : ${count} actions`;
            topHours.appendChild(li);
        });

        const recentUsers = $id('recent-users');
        data.recent_users.forEach(user => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${user.name}</td>
                <td>${user.age}</td>
                <td>${user.interests.join(', ')}</td>
                <td>${user.activity_count}</td>
            `;
            recentUsers.appendChild(tr);
        });

        $id('sample-name').textContent = data.sample_user.name;
        $id('sample-age').textContent = data.sample_user.age;
        $id('sample-interests').textContent = data.sample_user.interests.join(', ');
        $id('sample-activity').textContent = data.sample_user.activity_log.slice(0, 3).join(' | ');

        const suggestionsList = $id('suggestions-list');
        data.suggestions.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            suggestionsList.appendChild(li);
        });

        const similarList = $id('similar-suggestions-list');
        data.similar_suggestions.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            similarList.appendChild(li);
        });

        const todoList = $id('todo-list');
        data.todo.forEach(task => {
            const li = document.createElement('li');
            li.textContent = `${task.done ? '✅' : '🔲'} ${task.task}`;
            todoList.appendChild(li);
        });

        // Affichage des graphiques avec vérification des données
        if (data.interest_labels && data.interest_values) {
            buildChart('interestChart', 'bar', data.interest_labels, data.interest_values, 'Intérêts', 'rgba(79, 97, 216, 0.75)');
            buildChart('interestChart2', 'bar', data.interest_labels, data.interest_values, 'Intérêts', 'rgba(16, 185, 129, 0.75)');
        }
        
        if (data.hours && data.hourly_activity) {
            buildChart('hourlyChart', 'line', data.hours, data.hourly_activity, 'Activité horaire', 'rgba(37, 99, 235, 0.75)');
        }
        
        if (data.category_labels && data.category_values) {
            buildChart('categoryChart', 'bar', data.category_labels, data.category_values, 'Catégories d\'activité', 'rgba(245, 158, 11, 0.75)');
        }
    })
    .catch(error => {
        console.error('Impossible de charger les données:', error);
    });
