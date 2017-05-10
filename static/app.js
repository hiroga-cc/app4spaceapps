$(function () {
    'use strict';

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

function showModal(countryId) {

    // initialize modal
    initModal();

    if (countryId == 'usa') {
        return $('.start_modal_trigger_btn').trigger('click');
    }

    // modal 発火
    $('.modal_trigger_btn').trigger('click');

    // 問題文
    createMsgAndQuestions(countryId);
};

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

/* 3D描画 */

var map
var camera
var scene, group, mesh
var mouseX = 0, mouseY = 0;
var mouse = { x: 0, y: 0 };
var renderer
var stat

var windowHalfX = window.innerWidth / 2;
var windowHalfY = window.innerHeight / 2;

var projector = new THREE.Projector();

// 以下の値はこれから作成する3Dデータのプロパティである。
var r = 215; //地球の半径
var c_size = r/15; // 地球の半径に対する、スポットの円のサイズ

// 以下の値は読み込む画像に依存する。
var map_w = 1280;
var map_h = 640;
var map_xy = {
  "japan":{
    "x":600,"y":285
  }, "australia":{
    "x":640,"y":520
  }, "sounthafrica":{
    "x":165,"y":510
  }, "chile":{
    "x":1150,"y":525
  }, "germany":{
    "x":130,"y":220
  }, "usa":{
    "x":1120,"y":300
  }
};
var mesh_ary = [];

init()
animate()

function init(){
  map = document.getElementById("map")
  camera = new THREE.PerspectiveCamera(60, window.innerWidth/ window.innerHeight, 1, 2000)
  camera.position.z = 500

  scene = new THREE.Scene()
  group = new THREE.Group()
  scene.add(group)

  // earth
  var loader = new THREE.TextureLoader();
  loader.load( "static/worldmap.png", function ( texture ) {
    var geometry = new THREE.SphereGeometry( r, 16, 16 ); // 半径、水平切断面の辺の数、垂直切断面の〜
    var material = new THREE.MeshBasicMaterial( { map: texture, overdraw: 0.5 } );
    var mesh = new THREE.Mesh( geometry, material );
    group.add( mesh );

  } );


  var i = 0;
  for (key in map_xy){
    i = i+1;
    // 国別のスポットのメッシュ
    var mesh_color = 0xe01111;
    if (key == "usa"){mesh_color = 0x4011ff;}
    var material = new THREE.MeshBasicMaterial( { color: mesh_color } );
    var geometry = new THREE.CircleGeometry( c_size, 32 );
    var mesh = new THREE.Mesh( geometry, material );
    mesh.name=key;

    var xyz = returnXYZ(key);
    mesh.position.set(xyz["x"],xyz["y"],xyz["z"]);

    var rad_x = ((map_xy[key]["y"]-(map_h/2))/map_h) * (Math.PI);
    var rad_y = ((map_xy[key]["x"]-(map_w/4))/map_w) * (2*Math.PI);
    mesh.rotation.set(rad_x,rad_y,0);  // xはお辞儀、yはメリーゴーランド, zは車輪
    group.add( mesh );
    mesh_ary.push( mesh );
  };

  renderer = new THREE.CanvasRenderer()
  renderer.setClearColor( 0xffffff );
  renderer.setPixelRatio( window.devicePixelRatio );
  renderer.setSize( window.innerWidth, window.innerHeight );
  map.appendChild( renderer.domElement );

  // stats = new Stats()
  // map.appendChild(stats.dom)
  document.addEventListener( 'mousemove', onDocumentMouseMove, false );
  window.addEventListener( 'resize', onWindowResize, false );
}

function returnXYZ(country){
  var theta1,theta2; // 上記を元に割り出した、3Dに座標をマップした際の角度
  var x_,z_; //y=0におけるx,z座標
  var xyz = {};

  theta1 = map_xy[country]["x"] / (map_w/2) * Math.PI; //ex. 日本ならだいたい3
  theta2 = map_xy[country]["y"] / map_h * Math.PI; //ex./日本ならだいたい1.5
  x_ = Math.cos(theta1) * r;
  z_ = Math.sin(theta1) * r;
  xyz["x"] = x_ * Math.sin(theta2) * -1; //地図と3Dオブジェクトで座標の開始位置を揃えるため、マイナス反転が必要
  xyz["y"] = Math.cos(theta2) * r;
  xyz["z"] = z_ * Math.sin(theta2);
  return xyz;
}

function animate() {
  requestAnimationFrame( animate );
  render();
  // stats.update();
}
function render() {
  camera.lookAt( scene.position );
  group.rotation.x -=  mouseY * 0.0001;
  group.rotation.y -=  mouseX * 0.0001;
  renderer.render( scene, camera );
}

function onWindowResize() {
  windowHalfX = window.innerWidth / 2;
  windowHalfY = window.innerHeight / 2;
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize( window.innerWidth, window.innerHeight );
}

function onDocumentMouseMove( event ) {
  // このmouseXとYは、画面中央からのズレ度合いを示す
  mouseX = ( event.clientX - windowHalfX );
  mouseY = ( event.clientY - windowHalfY );
}
window.onmousedown = function(ev){
  if (ev.target == renderer.domElement){

    //マウス座標2D変換
    var rect = ev.target.getBoundingClientRect();
    mouse.x =  ev.clientX - rect.left;
    mouse.y =  ev.clientY - rect.top;

    width = window.innerWidth;
    height = window.innerHeight;

    //マウス座標3D変換 width（横）やheight（縦）は画面サイズ
    mouse.x =  (mouse.x / width) * 2 - 1;
    mouse.y = -(mouse.y / height) * 2 + 1;

    // マウスベクトル
    var vector = new THREE.Vector3( mouse.x, mouse.y ,1);

   // vector はスクリーン座標系なので, オブジェクトの座標系に変換
    projector.unprojectVector( vector, camera );

    // 始点, 向きベクトルを渡してレイを作成
    var ray = new THREE.Raycaster( camera.position, vector.sub( camera.position ).normalize() );
    var obj = ray.intersectObjects(mesh_ary)
    if (obj.length > 0){
      showModal(obj[0]['object'].name);
    }
  }
}
