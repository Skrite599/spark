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

    return false;
}

function submitDeck(form_data) {

    var request_body = {}

    if (form_data['deck_name'] && form_data['deck_score']) {
        request_body = {
            'deck_name' : form_data['deck_name'].value,
            'deck_score' : form_data['deck_score'].value
        }
    }

    var request_body = JSON.stringify(request_body);

    fetch('/api/deck', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: request_body
    }).then((response) => {
        response.json().then((data) => {
            if (data['status'] == 'success') window.location.href = '/';
        })
    }).catch((error) => {
        alert('Something Went Wrong' + error);
    });

    return false;
}

function submitGame(form_data) {

    var request_body = {};

    if (form_data['deck_name'] && form_data['game_win'] && form_data['game_loss']) {
        request_body = {
            'deck_name' : form_data['deck_name'].value,
            'game_win' : form_data['game_win'].value,
            'game_loss' : form_data['game_loss'].value
        }
    }

    var request_body = JSON.stringify(request_body);

    fetch('/api/game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: request_body
    }).then((response) => {
        response.json().then((data) => {
            if (data['status'] == 'success') window.location.href = '/';
        })
    }).catch((error) => {
        alert('Something Went Wrong' + error);
    });
    
    return false;
}

function login(form_data) {

    var request_body = {};

    if (form_data['username']) {
        request_body = {
            'username' : form_data['username'].value
        }
    }

    var request_body = JSON.stringify(request_body);
    
    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: request_body
    }).then((response) => {
        response.json().then((data) => {
            if (data['status'] == 'success') window.location.href = '/';
        })
    }).catch((error) => {
        alert('Something Went Wrong' + error);
    });

    return false;
}