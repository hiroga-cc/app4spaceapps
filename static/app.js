$(function () {

    $('.country').click(function () {
        $countryId = $(this).data('id');
        $('#' + $countryId + '_btn').trigger('click');
        var msg = getModalText($countryId);
        var input = getInput();
        // $('.modal-body').html(msg + input);
        $('p#msg').html(msg);

    });
    
    
    $('#save').click(function () {
        console.log('save clicked');
    });

    $('#go').click(function () {
        var select = getAnswer();
        $('p#select').html(select);
    });
    
    $('.answerRadio').click(function () {

        console.log('radio clicked');
    });
});

function getAnswer() {

    return '\
    <input type="radio" class="answerRadio" name="r1" value="1">aaa<br>\
        <input type="radio" class="answerRadio" name="r1" value="2">bbb<br>\
        <input type="radio" class="answerRadio" name="r1" value="3">ccc';
}

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
            msg = 'japan clicked';
            break;
        case 'c1' :
            msg = 'c1 clicked';
            break;
        case 'c2' :
            msg = 'c2 clicked';
            break;
    }
    return msg;
}
