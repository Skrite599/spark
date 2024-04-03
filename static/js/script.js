function populateSearch(e) {

    const searchText = e.value.toLowerCase();
    searchText.replace(/[.*+?^${}()|[\]\\]/g, '');
    const deckList = document.getElementById('deck-list');

    var pattern = `${searchText}`;

    var regex = new RegExp(pattern);
    
    Array.from(deckList.children).forEach(item => {
        const currentDeck = item.textContent.toLowerCase();
        
        if (currentDeck.match(regex)) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
    });
}

function submitDeck(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    fetch('/api/deck', {
        method: 'POST',
        body: formData
    }).then((response) => {
        console.log(response);
        if (response.ok) window.location.href = '/';
    }).catch(error => {
        alert('Something Went Wrong' + error);
    });
}

function submitGame(form_data) {

    var request_body = {};

    console.log(form_data);

    if (form_data['deck_name'] && form_data['game_win'] && form_data['game_loss']) {
        request_body = {
            'deck_name' : form_data['deck_name'].value,
            'game_win' : form_data['game_win'].value,
            'game_loss' : form_data['game_loss'].value
        }
    }

    var request_body = JSON.stringify(request_body);

    console.log(request_body);

    fetch('/api/game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: request_body
    }).then((response) => {
        response.json().then((data) => {
            console.log(data);
            if (data['status'] == 'success') window.location.href = '/';
        })
    }).catch(error => {
        alert('Something Went Wrong' + error);
    });
    
    return false;
}

function login(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);
    
    fetch(form.action, {
        method: form.method,
        body: formData
    }).then((response) => {
        console.log(response)
    }).catch(error => {
        alert('Something Went Wrong' + error);
    });
}