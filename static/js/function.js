document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const deckList = document.getElementById('deck-list');
    const deckForm = document.getElementById('submit-deck');

    // Search functionality
    if (searchInput) {
      searchInput.addEventListener('input', function() {
          const searchText = searchInput.value.toLowerCase();
          searchText.replace(/[.*+?^${}()|[\]\\]/g, '');
  
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
      });

        const deckProfile = deckList.querySelectorAll('li a');

        deckProfile.forEach(deckItem => {
          deckItem.addEventListener('click', function(e) {
            e.preventDefault();

            const headers = new Headers();
            headers.append('session-id', 'a06e2d2b-2245-4178-b652-720a71b95aa1')

            fetch(e.target.href, {
              headers: headers
            }).then(
              window.location.href = e.target.href
            ).catch(error => {
              alert('Something Went Wrong' + error)
            });
        });
      })
    }

    if (deckForm) {
      deckForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const form = e.target;
        const formData = new FormData(form);

        const headers = new Headers();
        headers.append('session-id', 'a06e2d2b-2245-4178-b652-720a71b95aa1');

        fetch(form.action, {
          method: form.method,
          headers: headers,
          body: formData
        }).then(
          window.location.href = '/'
        ).catch(error => {
          alert('Something Went Wrong' + error);
        });
      });
    }
});