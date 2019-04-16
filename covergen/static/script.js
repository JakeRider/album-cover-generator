function fetchAlbumJSON() {
  console.log('Fetching!');
}

function init() {
  newAlbumBtn = document.querySelector('#newAlbumBtn');
  newAlbumBtn.addEventListener('click', fetchAlbumJSON);
}

window.onload = init;
