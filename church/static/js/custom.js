// Example JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
  // Add smooth scrolling to all links
  var scrollLinks = document.querySelectorAll('.click-scroll');
  scrollLinks.forEach(function(link) {
      link.addEventListener('click', function(e) {
          e.preventDefault();
          document.querySelector(this.getAttribute('href')).scrollIntoView({
              behavior: 'smooth'
          });
      });
  });

  // Initialize Magnific Popup (example for video links)
  $('.popup-youtube').magnificPopup({
      type: 'iframe',
      mainClass: 'mfp-fade',
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false
  });
});
