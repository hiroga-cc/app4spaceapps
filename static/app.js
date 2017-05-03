$(function () {
    'use strict';

    $('.country').click(function () {

        var $countryId = (this.id);

        // initialize modal
        initModal();

        if ($countryId == 'usa') {
            return $('.start_modal_trigger_btn').trigger('click');
        }

        // modal 発火
        $('.modal_trigger_btn').trigger('click');

        // 問題文
        createMsgAndQuestions($countryId);

    });



    // click 選択肢
    $('#panel').on("click", ".click-able-panel", function () {
        var child = $(this).children();
        if ($(this).data('collect') === 'y') {
            // collect
            $(this).addClass('panel-success');
            child.removeClass('hidden');

            // next button
            $('#save').show();
        } else {
            // wrong
            $(this).addClass('panel-danger');
            child.removeClass('hidden');
        }
    });
});


/*
 * 問題文生成
 */
function createMsgAndQuestions(countryId) {
    // add 問題文
    $('p.msg').html(getModalText(countryId));

    // add 選択肢
    $('p.msg').append(makeQuestions(countryId));
}

/*
 * モーダル初期化
 */
function initModal() {
    var $panel_body = $('#panel').find('div.panel-body');
    $panel_body.html('');
    $('#save').hide();
}

/**
 * 選択肢生成
 */
function makeQuestions(countryId) {
    var question = null;
    switch (countryId) {
        case 'japan':
            question = {
                'n1': 'Post-Disaster Damage Determination(P3D)',
                'y': 'Earth Observatory Natural Event Tracker – News Feed'
            };
            break;

        case 'australia':
            question = {
                'n1': 'ADAM',
                'y': 'GeoAnalysis Drone'
            };
            break;

         case 'chile':
            question = {
                'n2': 'Martian Marathon',
                'n1': 'Friendly Couch',
                'y': 'AstroFit - Healthcare and fitness monitoring apps for astronauts'
            };
            break;

         case 'germany':
            question = {
                'n2': 'Long Jump Module',
                'y': 'marin robot autonomous',
                'n1': 'biochemical & mechanical prosses to generate renewable energy & reducethe operating energy of jetpack'
            };
            break;

       case 'southafrica':
            question = {
                'n2': 'HoloCube',
                'y': 'Iceinspec',
                'n1': 'Green Wave'
            };
            break;
    }

    var ret_q = '';

    for (var key in question) {
       var answer = (key == 'y') ? 'Collect' : 'Wrong';
       ret_q += '\
           <div  class="panel panel-default click-able-panel"  data-collect="'+ key +'">\
               <div class="panel-heading hidden">'+ answer +'</div>\
               <div class="panel-body" > '+ question[key] +' </div>\
           </div>';
    }
    return ret_q;
}

/*
 * 警告文生成
 */
function getModalText(countryId) {
    var msg = '';
    switch (countryId) {
        case 'japan' :
            msg = '地震発生時、発生前後の変化をみるにはどうすればいい？';
            break;
        case 'australia':
            msg = '水の少ない場所で、大規模農業をするためには、賢く水を使うのが大切だよ。空の上から、どうすればいい？';
            break;
        case 'southafrica' :
            msg = '南極海に船が向かうとき、最も南極に近い南アフリカ共和国などが拠点としてよく使用されるよ。天候の変化が激しい南極海で、安全に航海できるようにしてほしい！';
            break;

        case 'germany' :
            msg = 'ヨーロッパでは、環境に優しい海のエネルギーの研究が進められています。海の上の風や波のデータを蓄えるには、どんなSpace Appsを使えばいいかな？';
            break;

        case 'chile' :
            msg = '南アメリカへの旅行では、空気が薄い場所での高山病に気をつけないと。体の調子やどれだけ運動したかが一目で分かるようにできないかな？'
            break;

    }
    return msg;
}


