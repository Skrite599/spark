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
    const scoreElement = form_data.querySelector('.score.container ul');
    const deckListElement = form_data.querySelector('.deckInputContainer textarea')

    if (form_data['deck_name'] && scoreElement && deckListElement) {
        request_body = {
            'deck_name' : form_data['deck_name'].value,
            'deck_score' : scoreElement.innerText,
            'deck_list': deckListElement.value
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

function setToolTip(score) {

    const form_data = document.getElementById('deck')

    const tooltipContainer = document.querySelector('.form .tooltip.container');

    score = Number(score)

    const tooltipLow = form_data.querySelector('.tooltip.container .low');
    const tooltipMed = form_data.querySelector('.tooltip.container .med');
    const tooltipHigh = form_data.querySelector('.tooltip.container .high');
    const tooltipCEDH = form_data.querySelector('.tooltip.container .cedh');

    if (score >= 1 && score <= 5) {
        tooltipLow.style.display = 'block';
        tooltipMed.style.display = 'none';
        tooltipHigh.style.display = 'none';
        tooltipCEDH.style.display = 'none';
    } else if (score == 6) {
        tooltipLow.style.display = 'none';
        tooltipMed.style.display = 'block';
        tooltipHigh.style.display = 'none';
        tooltipCEDH.style.display = 'none';
    } else if (score >= 7 && score <= 9) {
        tooltipLow.style.display = 'none';
        tooltipMed.style.display = 'none';
        tooltipHigh.style.display = 'block';
        tooltipCEDH.style.display = 'none';
    } else if (score == 10) {
        tooltipLow.style.display = 'none';
        tooltipMed.style.display = 'none';
        tooltipHigh.style.display = 'none';
        tooltipCEDH.style.display = 'block';
    } else {
        tooltipLow.style.display = 'none';
        tooltipMed.style.display = 'none';
        tooltipHigh.style.display = 'none';
        tooltipCEDH.style.display = 'none';
    }

    tooltipContainer.classList.add('active');
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

function shiftScore(button) {

    const scoreValueDiv = document.querySelector('.score.container #value span');

    if (!scoreValueDiv.innerText || scoreValueDiv.innerText == '') return;

    const lowButton = document.querySelector(".score.container #level-selector button[value='low']");
    const medButton = document.querySelector(".score.container #level-selector button[value='med']");
    const highButton = document.querySelector(".score.container #level-selector button[value='high']");
    const cedhButton = document.querySelector(".score.container #level-selector button[value='cedh']");

    var scoreValue = scoreValueDiv.textContent;
    scoreValue = Number(scoreValue);

    if (button.classList.contains('prev') && scoreValue != 1) {
        scoreValue -= 1;
    } else if (button.classList.contains('next') && scoreValue != 10) {
        scoreValue += 1;
    }

    scoreValueDiv.innerText = scoreValue;

    if (scoreValue >= 1 && scoreValue <= 5) {
        shiftButton(lowButton);
    } else if (scoreValue == 6) {
        shiftButton(medButton);
    } else if (scoreValue >= 7 && scoreValue <= 9) {
        shiftButton(highButton);
    } else if (scoreValue == 10) {
        shiftButton(cedhButton);
    }

    // setToolTip(scoreValue);

}

function shiftButton(button) {

    const levelButtons = document.querySelectorAll('button.selector');

    levelButtons.forEach((levelButton) => {
        var classList_active = levelButton.classList;
        classList_active.remove('active');
    });

    button.classList.add('active');
}

function setScore(span) {

    if (!span) return;

    var score = 0;
    var level = span.innerText;
    const scoreValueDiv = document.querySelector('.score.container #value span');
    const arrowImgs = document.querySelectorAll('.score.container .direction img');

    if (level == 'Low') {
        score = 5;
    } else if (level == 'Medium') {
        score = 6;
    } else if (level == 'High') {
        score = 7;
    } else if (level == 'CEDH') {
        score = 10;
    }

    scoreValueDiv.innerText = score;
    arrowImgs.forEach((arrowImg) => {
        arrowImg.classList.add('active');
    });

    // setToolTip(score);
}

function toggleButton(button) {

    const levelButtons = document.querySelectorAll('button.selector');

    levelButtons.forEach((levelButton) => {
        var classList_active = levelButton.classList;
        classList_active.remove('active');
    });

    button.classList.add('active');

    setScore(button.querySelector('span'));
}

function displayMenu(navA) {
    var ultilityContainer = document.getElementById('link-container');
    if (ultilityContainer.style.display === "block") {
        ultilityContainer.style.display = "none";
    } else {
        ultilityContainer.style.display = "block";
    }
}

function displayInput(div) {
    const deckInput = document.querySelector('.form#deck .input.container#deck-input');
    const playerInput = document.querySelector('.form#game .input.container#player-input');
    
    div.style.display = 'none';

    if (deckInput) deckInput.style.display = 'block';
    if (playerInput) playerInput.style.display = 'block';
}