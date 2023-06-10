document.addEventListener('DOMContentLoaded', () => {
    const resetButton = document.getElementById('reset-button');
    resetButton.addEventListener('click', () => {
      fetch('/reset', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        if (response.status === 200) {
          window.location.reload();
        } else {
          console.error('Reset failed');
        }
      })
      .catch(error => {
        console.error('Reset failed:', error);
      });
    });
  });
  