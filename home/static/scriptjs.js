let likes = document.querySelector(".fa-heart");
let likes_count = document.querySelector(".like-count");
let share = document.querySelector(".share");

let count = parseInt(localStorage.getItem('likeCount')) || 0;
let liked = false; // Initially not liked

if (liked) {
  likes.classList.add('liked');
}

likes_count.innerHTML = count;

likes.addEventListener('click', () => {
  if (liked) {
    count--;
    likes_count.innerHTML = count;
    liked = false;
    likes.classList.remove('liked');
  } else {
    count++;
    likes_count.innerHTML = count;
    liked = true;
    likes.classList.add('liked');
    liked.setAttribute('backgroundColor' , 'red');
  }
  localStorage.setItem('likeCount', count);
});

share.addEventListener('click', () => {
  if (navigator.share) {
    navigator.share({
      title: 'Your post title',
      text: 'Your post description',
      url: 'google.com',
    })
      .then(() => console.log('Successful share'))
      .catch((error) => console.log('Error sharing', error));
  } else {
    console.log('Web Share API not supported');
  }
});