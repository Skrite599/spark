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

function submitGame(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    fetch('/api/game', {
        method: 'POST',
        body: formData
    }).then((response) => {
        console.log(response);
        if (response.ok) window.location.href = '/';
    }).catch(error => {
        alert('Something Went Wrong' + error);
    });
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