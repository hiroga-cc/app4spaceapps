$(function () {

    $('.country').click(function () {

        $countryId = $(this).data('id');

        if ($countryId == 'usa') {
            $('.start_modal_trigger_btn').trigger('click');
            return;
        }

        $('.modal_trigger_btn').trigger('click');
        var msg = getModalText($countryId);
        var input = getInput();
        $('p#msg').html(msg);

    });


    $('#save').click(function () {
        console.log('save clicked');
    });

    $('#go').click(function () {
        var select = getanswer();
    });

    $('.answerRadio').click(function () {
        console.log('radio click');
    });
});



function getInput() {
    // return '
    // <div class="input-group">\
    //   <input type="text" class="form-control" placeholder="answer" aria-describedby="basic-addon1">\
    //   <span class="input-group-btn">\
    //     <button class="btn btn-primary" id="go" type="button">Go!</button>\
    //   </span>\
    // </div>';
}



function getModalText(countryId) {
    var msg = null;
    switch (countryId) {
        case 'japan' :
            msg = '地震発生時、発生前後の変化をみるにはどうすればいい？';
            break;
        case 'australia':
            msg = 'australia clicked';
            break;
        case 'southafrica' :
            msg = 'southafrica clicked';
            break;
        case 'southafrica' :
            msg = 'southafrica clicked';
            break;
        case 'southafrica' :
            msg = 'southafrica clicked';
            break;

    }
    return msg;
}


