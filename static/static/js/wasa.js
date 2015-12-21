// ADD BOOTSTRAP.JS

// STRIPE
function stripeResponseHandler(status, response){
      var $form = $('#payment-form');

      if (response.error) {
        // Show the errors on the form
        $form.find('.payment-errors').text(response.error.message);
        $form.find('button').prop('disabled', false);
      } else {
        // response contains id and card, which contains additional card details
        var token = response.id;
        // Insert the token into the form so it gets submitted to the server
        $form.append($('<input type="hidden" name="stripeToken" />').val(token));
        // and submit
        $form.get(0).submit(); 
      }

      jQuery(function($) {
          $('#payment-form').submit(function(event) {
            var $form = $(this);
            // Disable the submit button to prevent repeated clicks
            $form.find('button').prop('disabled', true);
            Stripe.card.createToken($form, stripeResponseHandler);
            // Prevent the form from submitting with the default action
            return false;
          });
      });
};

// carousel 
$(document).ready(function(){

    if ($(window).width() > 1900) {
        $('#image-container').removeClass('container');
    };

    $(".carousel").carousel({
      "interval": 2500
    })
});


// FORM-VALIDATION.JS Form input validator needs to be updated, changed to moving 
$(document).ready(function(){
   
   

    // SUCCESS AND ERROR FORM GLYPHS
    // success glyphs
    // <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
    // <span id="inputSuccess2Status" class="sr-only">(success)</span> aria-describedby="inputSuccess2Status"

    // error glyphs
    // <span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true"></span>
    // <span id="inputError2Status" class="sr-only">(error)</span>
    // remove default error message and replace with bootstrap box highlighting and text
    // $.validator.setDefaults({
    //     // errorClass: '', // sets class of error message
    //     // errorElement: ''  // sets element
    //     // For testing only
    // });

    // field validator 
    // take the validation rules out of form template
    $('#regForm').validate({
        rules: {
            email: {
              required: true,
              email: true
            },

            first_Name: 'required',
            last_Name: 'required',
            city: 'required',
            zip_code: 'required',
            state: 'required',
            work_phone: 'required',
            cell_phone: 'required',
            street_address : 'required',
            company: 'required'

        },
    }); 
    
    // basic form validator and submission
    $("#regForm").validate({ 
      submitHandler: function(form) {  
      if ($(form).valid()) 
        form.submit(); 
        return false; // prevent normal form posting
      }
    });

       
});






