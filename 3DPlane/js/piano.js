//piano var
var wKeyIndex=0;
var bKeyIndex=0;

var Piano = function(){
  this.mesh = new THREE.Object3D();
  this.mesh.name = "piano";

  //White Keys
  

  var wkGeom = new THREE.BoxGeometry(1,5,1,1,1,1);
  var wkMat = new THREE.MeshPhongMaterial({color:Colors.white, shading:THREE.FlatShading});
  var wk = new THREE.Mesh(wkGeom, wkMat);
  wk.geometry.applyMatrix(new THREE.Matrix4().makeTranslation(0,2,0));
  var wks = new THREE.Object3D();

  this.wkTop = new THREE.Object3D();

  for (var i=0;i<52;i++){
    var key = wk.clone();
    key.position.set(-26+i*1,20,0);
    key.castShadow = true;
    key.receiveShadow = true;
    key.geometry.applyMatrix(new THREE.Matrix4().makeScale(1,1,1));
    this.wkTop.add(key);
  }
  
  wks.add(this.wkTop);

  this.mesh.add(wks);

  //Black Keys
  var bwidth=0.7   //width of black keys
  var bkGeom = new THREE.BoxGeometry(bwidth,3,0.5,1,1,1);
  var bkMat = new THREE.MeshPhongMaterial({color:Colors.black, shading:THREE.FlatShading});
  var bk = new THREE.Mesh(bkGeom, bkMat);
  bk.geometry.applyMatrix(new THREE.Matrix4().makeTranslation(0,2,0));
  var bks = new THREE.Object3D();

  this.bkTop = new THREE.Object3D();

  for (var i=0;i<36;i++){
    var key = bk.clone();
    var locs=[1,3,4,6,7,8,10,11,13,14,15,17,18,20,21,22,24,25,27,28,29,31,32,34,35,36,38,39,41,42,43,45,46,48,49,50];
    key.position.set(-26+locs[i]-bwidth/2,21,0.5);
    key.castShadow = true;
    key.receiveShadow = true;
    key.geometry.applyMatrix(new THREE.Matrix4().makeScale(1,1,1));
    this.bkTop.add(key);
  }
  
  bks.add(this.bkTop);

  this.mesh.add(bks);

};

Piano.prototype.updateWks = function(){
  //*
  var wks = this.wkTop.children;
  //*
  if ((wKeyIndex>0)&&(wKeyIndex<53)){
    var oldKey = wks[wKeyIndex-1];
    oldKey.position.z+=0.5;
  }
  //*/
  
  if (wKeyIndex<52){
    wKeyIndex=wKeyIndex%52;
    var key = wks[wKeyIndex];
    key.position.z-=0.5;
    //key.position.z++;
    wKeyIndex++;
    //*/
  }

}

function createPiano(){
  piano = new Piano();
  piano.mesh.scale.set(6,6,6);
  piano.mesh.position.y = game.planeDefaultHeight;
  scene.add(piano.mesh);
}

updatePiano();

function updatePiano(){
  piano.updateWks();
}

createPiano();