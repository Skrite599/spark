function populateSearch(input_data) {

    var searchQuery = input_data.value.toLowerCase();
    searchQuery.replace(/[.*+?^${}()|[\]\\]/g, '');
    var searchText = "(^" + searchQuery + "| " + searchQuery + ")";
    const searchResult = document.getElementById('result-container');
    const userResultContainer = document.getElementById('user-results');

    if (input_data.value == '' || input_data.value == null) {
        searchResult.style.display = 'none';
        userResultContainer.style.display = 'none';
        return false;
    }

    var pattern = `${searchText}`;

    var regexQuery = new RegExp(pattern);

    populateDeckResults(regexQuery);
    populateUserResults(searchQuery);

    searchResult.style.display = 'block';

    return false;
}

function populateDeckResults(query) {

    const deckList = document.querySelectorAll('#deck-list li');
    deckList.forEach((item) => {
        const currentDeck = item.textContent.toLowerCase();
        
        if (currentDeck.match(query)) {
          item.style.display = 'block';

        } else {
          item.style.display = 'none';
        }
    });
}

async function populateUserResults(query) {

    var users = [];
    const userList = document.getElementById('user-list');
    const userResultContainer = document.getElementById('user-results');
    userList.innerHTML = '';

    users = await fetch('/api/users/?search=' + query, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).catch((error) => {
        console.log('error', error);
    });

    users = await users.json();

    if (users['status'] == 'error') {
        userList.innerHTML = '';
        return;
    }

    users['data'].forEach((user) => {
        var newLi = document.createElement('li');
        var newA = document.createElement('a');
        var newDiv = document.createElement('div');

        newA.id = 'user-' + user['user_id'];
        newA.href = '/user/' + user['user_id'];
        newA.textContent = user['username'];

        newDiv.id = 'individual-result-container';

        newLi.appendChild(newA);
        newDiv.appendChild(newLi);
        userList.appendChild(newDiv);
    });

    userResultContainer.style.display = 'block';
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

    if (form_data['deck_name'] && form_data['record']) {
        record = 0;
        form_data['record'].forEach((item) => {
            if (item.checked && item.id == 'game-win') {
                record += 1;
            } else if (item.checked && item.id == 'game-loss') {
                record -= 1;
            }
        });

        request_body = {
            'deck_name' : form_data['deck_name'].value,
            'record' : record
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
            else if (data['status'] == 'error' && data['message'] == 'user does not exist') window.location.href = '/sign-up'
        })
    }).catch((error) => {
        alert('Something Went Wrong' + error);
    });

    return false;
}

function logout() {

    fetch('/api/logout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        response.json().then((data) => {
            if (data['status'] == 'success') window.location.href = '/';
        })
    }).catch((error) => {
        alert('Something Went Wrong' + error);
    });

    return false;
}

function signup(form_data) {

    var request_body = {};

    if (form_data['username'] && form_data['email']) {
        request_body['username'] = form_data['username'].value
        request_body['email'] = form_data['email'].value
    }

    request_body = JSON.stringify(request_body);

    fetch('/api/signup', {
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