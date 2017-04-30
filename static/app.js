$(function () {

    $('.country').click(function () {

        $countryId = $(this).data('id');

        
        console.log($countryId);
        
        if ($countryId == 'usa') {
            $('.start_modal_trigger_btn').trigger('click');
            return;
        }

        // modal 発火
        $('.modal_trigger_btn').trigger('click');

        // 各国のパネルを表示
        $('#panel_' + $countryId ).removeClass('hidden');

        var msg = getModalText($countryId);
        // $('p#msg_' + $countryId).html(msg);
        $('p.msg').html(msg);

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
    
    $('.clickable-panel').click(function () {
        var collect = $(this).data('collect');
        var child = $(this).children();
        if (collect === 'y') {
            // 正誤
            $(this).addClass('panel-success');
            child.removeClass('hidden');

            // next botton
            $('#save').removeClass('hidden');

        } else {
            // 正誤
            $(this).addClass('panel-danger');
            child.removeClass('hidden');
        }
        
    });
    
    
});



// function getInput() {
    // return '
    // <div class="input-group">\
    //   <input type="text" class="form-control" placeholder="answer" aria-describedby="basic-addon1">\
    //   <span class="input-group-btn">\
    //     <button class="btn btn-primary" id="go" type="button">Go!</button>\
    //   </span>\
    // </div>';
// }



function getModalText(countryId) {
    var msg = null;
    switch (countryId) {
        case 'japan' :
            msg = '地震発生時、発生前後の変化をみるにはどうすればいい？';
            break;
        case 'australia':
            msg = '水の少ない場所で、大規模農業をするためには、賢く水を使うのが大切だよ。空の上から、どうすればいい？';
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


