// Admin Panel JavaScript

// Handle form submission
document.getElementById('admin-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const title = document.getElementById('content-title').value;
    const body = document.getElementById('content-body').value;
    const image = document.getElementById('content-image').files[0];

    if (!title || !body || !image) {
        alert('Please fill in all fields and select an image.');
        return;
    }

    const formData = new FormData();
    formData.append('title', title);
    formData.append('body', body);
    formData.append('image', image);

    // Simulate a backend request
    console.log('Uploading content...');
    console.log(`Title: ${title}`);
    console.log(`Body: ${body}`);
    console.log(`Image: ${image.name}`);

    // For actual backend integration, use fetch:
    // fetch('/upload', {
    //     method: 'POST',
    //     body: formData
    // })
    // .then(response => response.json())
    // .then(data => console.log(data))
    // .catch(error => console.error('Error:', error));

    alert('Content uploaded successfully!');
    document.getElementById('admin-form').reset();
});
let currentSlide= 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.slides img');
    slides.forEach((slide, i) => {
        slide.style.display = i === index ? 'block' : 'none';
    });
}

function nextSlide() {
    const slides = document.querySelectorAll('.slides img');
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

setInterval(nextSlide, 3000); // Change image every 3 seconds
showSlide(currentSlide);
let currentSlideb= 0;
constslides = document.querySelectorAll('.book-slide');

// Function to display the correct slide
function showSlide(index) {
    // Hide all slides
    slides.forEach(slide => {
        slide.style.display = 'none';
    });
    
    // Show the slide at the current index
    slides[index].style.display = 'block';
}

// Function to go to the next slide
function nextSlide() {
    if (currentSlide < slides.length - 1) {
        currentSlide++;
        showSlide(currentSlide);
    }
}

// Function to go to the previous slide
function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
        showSlide(currentSlide);
    }
}

// Set up initial display (show the first slide)
document.addEventListener('DOMContentLoaded', () => {
    showSlide(currentSlide);
});
letcurrentSlide = 0;
const slides= document.querySelectorAll('.book-slide');

// Function to display the correct slide
function showSlide(index) {
    // Hide all slides
    slides.forEach(slide => {
        slide.style.display = 'none';
    });
    
    // Show the slide at the current index
    slides[index].style.display = 'block';
}

// Function to go to the next slide
function nextSlide() {
    if (currentSlide < slides.length - 1) {
        currentSlide++;
        showSlide(currentSlide);
    }
}

// Function to go to the previous slide
function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
        showSlide(currentSlide);
    }
}

// Set up initial display (show the first slide)
document.addEventListener('DOMContentLoaded', () => {
    showSlide(currentSlide);
});
letcurrentSlide = 0;
constslides = document.querySelectorAll('.book-slide');

// Function to display the correct slide
function showSlide(index) {
    // Hide all slides
    slides.forEach(slide => {
        slide.style.display = 'none';
    });
    
    // Show the slide at the current index
    slides[index].style.display = 'block';
}

// Function to go to the next slide
function nextSlide() {
    if (currentSlide < slides.length - 1) {
        currentSlide++;
        showSlide(currentSlide);
    }
}

// Function to go to the previous slide
function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
        showSlide(currentSlide);
    }
}

// Set up initial display (show the first slide)
document.addEventListener('DOMContentLoaded', () => {
    showSlide(currentSlide);
});
// Preload images to ensure smooth loading
const preloadImages = [
    'flower-pattern.jpg',  // Replace with actual image paths
    'hamlet-theme.jpg',    // Replace with actual image paths
    'modern-literature.jpg', // Replace with actual image paths
];

const preload = () => {
    preloadImages.forEach((image) => {
        const img = new Image();
        img.src = image;
    });
};

// Preload images when the page is loaded
window.onload = preload;
// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 1000, // Animation duration in milliseconds
    once: true, // Animation happens once
    easing: 'ease-in-out', // Easing function for animation
});
document.getElementById('commentForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get form values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    if (name && email && message) {
        // Show the thank-you message
        document.getElementById('thanks-message').classList.remove('hidden');

        // Clear the form
        document.getElementById('commentForm').reset();
    }
});
document.getElementById('registerForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.message === 'User registered successfully') {
            window.location.href = 'login.html';
        }
    });
});
document.addEventListener('DOMContentLoaded', function() {
    fetch('/index')
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('welcome-message').innerText = data.message;
        });
});
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
  };
  // Function to display a login message
function showLoginMessage() {
    alert("Login functionality is optional! You can access all content without logging in.");
  }
  const express = require('express');
  const session = require('express-session');
  const bodyParser = require('body-parser');
  
  const app = express();
  
  // Middleware
  app.use(bodyParser.urlencoded({ extended: true }));
  app.use(express.json());
  app.use(
      session({
          secret: 'secret-key', // Replace with a secure key
          resave: false,
          saveUninitialized: true,
          cookie: { maxAge: 60000 } // Session expires in 1 minute
      })
  );
  
  // In-memory user data for simplicity
  const users = {
      admin: 'password123',
      user1: 'mypassword'
  };
  
  // Login endpoint
  app.post('/login', (req, res) => {
      const { username, password } = req.body;
      if (users[username] && users[username] === password) {
          req.session.user = { username };
          res.json({ success: true, username });
      } else {
          res.status(401).json({ success: false, message: 'Invalid credentials' });
      }
  });
  
  // Logout endpoint
  app.post('/logout', (req, res) => {
      req.session.destroy((err) => {
          if (err) {
              return res.status(500).json({ success: false, message: 'Logout failed' });
          }
          res.json({ success: true });
      });
  });
  
  // Session status endpoint
    