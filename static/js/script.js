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

    // if (form_data['deck_name'] && form_data['game_win'] && form_data['game_loss']) {
    //     request_body = {
    //         'deck_name' : form_data['deck_name'],
    //         'game_win' : form_data['game_win'],
    //         'game_loss' : form_data['game_loss']
    //     }
    // }

    form_data.forEach((value, key) => {
        request_body[key] = value;
    });

    var request_body = JSON.stringify(jsonData);

    console.log(request_body);

    fetch('/api/game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: request_body
    }).then((response) => {
        console.log(response);
        if (response['status'] == 'success') window.location.href = '/';
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