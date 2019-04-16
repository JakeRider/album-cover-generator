async function fetchAlbumJSON() {
  const response = await fetch('/api/v1/album/generate-random');
  const json = await response.json();

  return json;
}

async function updateAlbum() {
  albumTitle = document.querySelector('#albumTitle');
  albumArtist = document.querySelector('#albumArtist');
  albumData = await fetchAlbumJSON();

  albumTitle.textContent = albumData.title;
  albumArtist.textContent = albumData.artist;
}

function init() {
  newAlbumBtn = document.querySelector('#newAlbumBtn');
  newAlbumBtn.addEventListener('click', updateAlbum);
}

window.onload = init;
