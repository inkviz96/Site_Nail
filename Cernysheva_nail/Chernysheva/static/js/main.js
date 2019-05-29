






function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

jQuery(function($){
  $('.load-more').on('click', function(e){
    e.prevebtDefault();
    const btn =$(this);
    const loader = btn.find('span');
    $.ajax({
      url: '',
      data: {'csrfmiddlewaretoken': getCookie('csrftoken'),
      name_of_client: $('name_of_client').val(),
      second_name_of_client: $('second_name_of_client').val(),
      phone_number_of_client: $('phone_number_of_client').val(),
      chooise_appointment_service: $('chooise_appointment_service').val(),
      date_and_time_appointment: $('date_and_time_appointment').val(),
    },
      type: 'POST',
    beforeSend:function(){
      btn.attr('disabled', true);
      loader.addClass('d-inline-block');
      console.log('\nbeforeSend\n');
    },
    success:function(responce){
      function(){
        alert('Запись прошла успешно!');
        loader.removeClass('d-inline-block');
        btn.attr('disabled', false);
        console.log(responce);
        console.log('\nsuccess\n');
      },
    },
    error: function(){
      alert('Error!');
      loader.removeClass('d-inline-block');
      btn.attr('disabled', false);
      console.log('\nerror\n');
    }
   });
  });
});
