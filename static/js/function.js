document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const deckList = document.getElementById('deck-list');
    const deckForm = document.getElementById('submit-deck');
    const loginForm = document.getElementById('login-form');
    const gameForm = document.getElementById('submit-game');

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

      // const deckProfile = deckList.querySelectorAll('li a');

      // deckProfile.forEach(deckItem => {
      //   deckItem.addEventListener('click', function(e) {
      //     e.preventDefault();

      //     fetch(e.target.href, {
      //     }).then(
      //       window.location.href = e.target.href
      //     ).catch(error => {
      //       alert('Something Went Wrong' + error)
      //     });
      //   });
      // })
    }

    if (deckForm) {
      deckForm.addEventListener('submit', function(e) {
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
      });
    }

    if (loginForm) {
      loginForm.addEventListener('submit', function(e) {
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
      });
    }

    if (gameForm) {
      gameForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const form = e.target;
        const formData = new FormData(form);

        fetch(form.action, {
          method: form.method,
          body: formData
        }).then((response) => {
          console.log(response);
          if (response['status'] == 200) {
            window.location.href = '/'
          }
        }).catch(error => {
          alert('Something Went Wrong' + error);
      });
    })
  }
});