let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

function giveCoal(element) {
    // const userId = element.getAttribute('data-user-id'); 
    // const wishListId = element.getAttribute('data-wish-list-id'); 

    fetch(`/list/${userId}/coal/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ wish_list_id: wishListId }),
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(text => { throw new Error(text); });
        }
        return response.json();
    })
    .then(data => {
        if (data.coaled) {
            element.classList.add('coaled');
        } else {
            element.classList.remove('coaled');
        }
        document.getElementById('coal-count').textContent = data.coal_count;
        
        // Toggle the button color
        element.classList.toggle('clicked');
    })
    .catch(error => console.error('Error:', error));
}