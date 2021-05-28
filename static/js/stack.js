$(document).ready(function(){

  var forms = $('form');

    // Whenever a button is clicked
  $(':button').on('click', function(e){

    // Get the current form and the button name
    var $form = $(this).parentsUntil('form');
    var button_name = $(this).attr('name');

    // Validate the form unless going backwards
    if(validate($form) || button_name === 'previous'){

        switch(button_name) {
        case 'next':
            // Next
            next_form();
            break;
        case 'previous':
            // Previous
            prev_form();
            break;
        case 'submit' :
                // Submit
            submit_forms();
            break;
        default:
            // Do nothing
        }

    }else{
        // Form not valid
    }

  });

  // Show next
  function next_form(){
    // Get all visible forms
    var visible_forms = $('form:visible');

    // Get the last form in the array
    var $current_form = $(visible_forms).last();

    // Get the next form
    var $next_form = $current_form.next();

    // Handle visibility of buttons
    $current_form.find(':button').css('visibility','hidden');

    // Show the next form
    $next_form.fadeIn();
  }

  // Show previous
  function prev_form(){
    var visible_forms = $('form:visible');
    var $current_form = $(visible_forms).last();
    var $prev_form = $current_form.prev();
    $prev_form.find(':button').css('visibility','visible');
    $current_form.fadeOut();
  }

  // Submit
  function submit_forms(){

    // All forms are valid
    // Create new form programically that contains all form elements
    // Submit it
    var form_data = forms.find('input:not(:button)').clone();
    var action = '/echo/html/';
    var method = 'POST';
    var $full_form = $('<form/>').attr({
        action: action,
      method: method
    }).append(form_data);

    // Submit the form
    $full_form.appendTo('body').css('display','none').submit();

  }

})

// Validate expects jQuery object
function validate($form){

  // Set valid to true
  var valid = true;

  // Any invalid element will set valid to false
  $.each($form.find('input:not(:button)'), function(index, input){
    // Utilizing HTML5 validation
    if(!input.checkValidity()){
        valid = false;
    }
  })

    return valid;
}