async function fetchAlbumJSON() {
  const response = await fetch('/api/v1/album/generate-random');
  const json = await response.json();

  return json;
}

async function updateAlbum() {
  album = document.querySelector('#album');
  albumTitle = document.querySelector('#albumTitle');
  albumArtist = document.querySelector('#albumArtist');
  albumData = await fetchAlbumJSON();
  cacheBuster = new Date().getTime();

  album.style.backgroundImage = `linear-gradient(black, black), url('https://source.unsplash.com/random/600x600?sig=${cacheBuster})`;

  albumTitle.textContent = albumData.title;
  albumArtist.textContent = albumData.artist;
}

function init() {
  newAlbumBtn = document.querySelector('#newAlbumBtn');
  newAlbumBtn.addEventListener('click', updateAlbum);
}

window.onload = init;
