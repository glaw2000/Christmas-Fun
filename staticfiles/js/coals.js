let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

function giveCoal(userId) {
    fetch(`/list/${userId}/coal/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({}),
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(text => { throw new Error(text); });
        }
        return response.json();
    })
    .then(data => {
        const coalButton = document.getElementById('coal-button');
        if (data.coaled) {
            coalButton.classList.add('coaled');
        } else {
            coalButton.classList.remove('coaled');
        }
        document.getElementById('coal-count').textContent = data.coal_count;
        
        // Toggle the button color
        coalButton.classList.toggle('clicked');
    })
    .catch(error => console.error('Error:', error));
}