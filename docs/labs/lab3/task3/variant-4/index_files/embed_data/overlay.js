google.maps.__gjsload__('overlay', function(_){var ks=function(a){this.g=a},Qka=function(){},ls=function(a){a.Mm=a.Mm||new Qka;return a.Mm},Rka=function(a){this.Fa=new _.Uh(function(){var b=a.Mm;if(a.getPanes()){if(a.getProjection()){if(!b.Ol&&a.onAdd)a.onAdd();b.Ol=!0;a.draw()}}else{if(b.Ol)if(a.onRemove)a.onRemove();else a.remove();b.Ol=!1}},0)},Ska=function(a,b){function c(){return _.Vh(e.Fa)}var d=ls(a),e=d.Sk;e||(e=d.Sk=new Rka(a));_.Va(d.ka||[],_.L.removeListener);var f=d.Oa=d.Oa||new _.Lq,g=b.__gm;f.bindTo("zoom",g);f.bindTo("offset",g);
f.bindTo("center",g,"projectionCenterQ");f.bindTo("projection",b);f.bindTo("projectionTopLeft",g);f=d.jq=d.jq||new ks(f);f.bindTo("zoom",g);f.bindTo("offset",g);f.bindTo("projection",b);f.bindTo("projectionTopLeft",g);a.bindTo("projection",f,"outProjection");a.bindTo("panes",g);d.ka=[_.L.addListener(a,"panes_changed",c),_.L.addListener(g,"zoom_changed",c),_.L.addListener(g,"offset_changed",c),_.L.addListener(b,"projection_changed",c),_.L.addListener(g,"projectioncenterq_changed",c)];c();b instanceof
_.Cf&&(_.O(b,"Ox"),_.Zk("Ox","-p",a))},Wka=function(a){if(a){var b=a.getMap();if(Tka(a)!==b&&b&&b instanceof _.Cf){var c=b.__gm;c.overlayLayer?a.__gmop=new Uka(b,a,c.overlayLayer):c.h.then(function(d){d=d.ac;var e=new ms(b,d);d.Xa(e);c.overlayLayer=e;Vka(a);Wka(a)})}}},Vka=function(a){if(a){var b=a.__gmop;b&&(a.__gmop=null,_.$k("Ox","-p",b.g),b.g.unbindAll(),b.g.set("panes",null),b.g.set("projection",null),b.i.pf(b),b.h&&(b.h=!1,b.g.onRemove?b.g.onRemove():b.g.remove()))}},Tka=function(a){return(a=
a.__gmop)?a.map:null},Uka=function(a,b,c){this.map=a;this.g=b;this.i=c;this.h=!1;_.O(this.map,"Ox");_.Zk("Ox","-p",this.g);c.Ce(this)},Xka=function(a,b){a.g.get("projection")!=b&&(a.g.bindTo("panes",a.map.__gm),a.g.set("projection",b))},ms=function(a,b){this.j=a;this.i=b;this.g=null;this.h=[]};_.D(ks,_.M);
ks.prototype.changed=function(a){"outProjection"!=a&&(a=!!(this.get("offset")&&this.get("projectionTopLeft")&&this.get("projection")&&_.Ge(this.get("zoom"))),a==!this.get("outProjection")&&this.set("outProjection",a?this.g:null))};var ns={};_.D(Rka,_.M);ns.Ce=function(a){if(a){var b=a.getMap();(ls(a).Qp||null)!==b&&(b&&Ska(a,b),ls(a).Qp=b)}};ns.pf=function(a){var b=ls(a),c=b.Oa;c&&c.unbindAll();(c=b.jq)&&c.unbindAll();a.unbindAll();a.set("panes",null);a.set("projection",null);b.ka&&_.Va(b.ka,_.L.removeListener);b.ka=null;b.Sk&&(b.Sk.Fa.ud(),b.Sk=null);_.$k("Ox","-p",a);delete ls(a).Qp};var os={};Uka.prototype.draw=function(){this.h||(this.h=!0,this.g.onAdd&&this.g.onAdd());this.g.draw&&this.g.draw()};ms.prototype.dispose=function(){};ms.prototype.zc=function(a,b,c,d,e,f,g,h){var k=this.g=this.g||new _.Lm(this.j,this.i,function(){});k.zc(a,b,c,d,e,f,g,h);a=_.A(this.h);for(b=a.next();!b.done;b=a.next())b=b.value,Xka(b,k),b.draw()};ms.prototype.Ce=function(a){this.h.push(a);this.g&&Xka(a,this.g);this.i.refresh()};ms.prototype.pf=function(a){_.bb(this.h,a)};os.Ce=Wka;os.pf=Vka;_.pf("overlay",{co:function(a){if(a){(0,ns.pf)(a);(0,os.pf)(a);var b=a.getMap();b&&(b instanceof _.Cf?(0,os.Ce)(a):(0,ns.Ce)(a))}},preventMapHitsFrom:function(a){_.qn(a,{onClick:function(b){return _.Vm(b.event)},Vc:function(b){return _.Sm(b)},Lg:function(b){return _.Tm(b)},Hd:function(b){return _.Tm(b)},hd:function(b){return _.Um(b)}}).Ah(!0)},preventMapHitsAndGesturesFrom:function(a){a.addEventListener("click",_.tf);a.addEventListener("contextmenu",_.tf);a.addEventListener("dblclick",_.tf);a.addEventListener("mousedown",
_.tf);a.addEventListener("mousemove",_.tf);a.addEventListener("MSPointerDown",_.tf);a.addEventListener("pointerdown",_.tf);a.addEventListener("touchstart",_.tf);a.addEventListener("wheel",_.tf)}});});