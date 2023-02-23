const loading = document.getElementById('loading');
const form = document.querySelector('form');
const tem = document.getElementById('temperature');
const num = document.getElementById('temperature-value');

form.addEventListener('submit', () => {
  loading.style.display = 'block';
});

function show(){

  num.value = tem.value;
}

$(document).ready(function() {
    $('.features-toggle button').click(function() {
        $('.features-section').animate({right: 0}, 500);
    });
    $('.features-section').click(function(event) {
        if (!$(event.target).closest('.features-list').length) {
            $('.features-section').animate({right: -300}, 500);
        }
    });
});
