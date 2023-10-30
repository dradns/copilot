"use strict";(self.webpackChunkmermaid_viewer=self.webpackChunkmermaid_viewer||[]).push([[984],{1984:function(t,e,a){a.r(e),a.d(e,{diagram:function(){return g}});var r=a(1562),i=a(8225),n=a(1818),d=a(8433),o=a(366),s=a(4855),l=(a(7892),a(504),a(8703),{}),p=function(t){var e=Object.entries(l).find((function(e){return e[1].label===t}));if(e)return e[0]},c={draw:function(t,e,a,r){var c=(0,o.c)().class;l={},o.l.info("Rendering diagram "+t);var g,h=(0,o.c)().securityLevel;"sandbox"===h&&(g=(0,i.Ys)("#i"+e));var u,f="sandbox"===h?(0,i.Ys)(g.nodes()[0].contentDocument.body):(0,i.Ys)("body"),x=f.select("[id='".concat(e,"']"));(u=x).append("defs").append("marker").attr("id","extensionStart").attr("class","extension").attr("refX",0).attr("refY",7).attr("markerWidth",190).attr("markerHeight",240).attr("orient","auto").append("path").attr("d","M 1,7 L18,13 V 1 Z"),u.append("defs").append("marker").attr("id","extensionEnd").attr("refX",19).attr("refY",7).attr("markerWidth",20).attr("markerHeight",28).attr("orient","auto").append("path").attr("d","M 1,1 V 13 L18,7 Z"),u.append("defs").append("marker").attr("id","compositionStart").attr("class","extension").attr("refX",0).attr("refY",7).attr("markerWidth",190).attr("markerHeight",240).attr("orient","auto").append("path").attr("d","M 18,7 L9,13 L1,7 L9,1 Z"),u.append("defs").append("marker").attr("id","compositionEnd").attr("refX",19).attr("refY",7).attr("markerWidth",20).attr("markerHeight",28).attr("orient","auto").append("path").attr("d","M 18,7 L9,13 L1,7 L9,1 Z"),u.append("defs").append("marker").attr("id","aggregationStart").attr("class","extension").attr("refX",0).attr("refY",7).attr("markerWidth",190).attr("markerHeight",240).attr("orient","auto").append("path").attr("d","M 18,7 L9,13 L1,7 L9,1 Z"),u.append("defs").append("marker").attr("id","aggregationEnd").attr("refX",19).attr("refY",7).attr("markerWidth",20).attr("markerHeight",28).attr("orient","auto").append("path").attr("d","M 18,7 L9,13 L1,7 L9,1 Z"),u.append("defs").append("marker").attr("id","dependencyStart").attr("class","extension").attr("refX",0).attr("refY",7).attr("markerWidth",190).attr("markerHeight",240).attr("orient","auto").append("path").attr("d","M 5,7 L9,13 L1,7 L9,1 Z"),u.append("defs").append("marker").attr("id","dependencyEnd").attr("refX",19).attr("refY",7).attr("markerWidth",20).attr("markerHeight",28).attr("orient","auto").append("path").attr("d","M 18,7 L9,13 L14,7 L9,1 Z");var y=new d.k({multigraph:!0});y.setGraph({isMultiGraph:!0}),y.setDefaultEdgeLabel((function(){return{}}));for(var v=r.db.getClasses(),b=0,m=Object.keys(v);b<m.length;b++){var w=m[b],k=v[w],E=s.s.drawClass(x,k,c,r);l[E.id]=E,y.setNode(E.id,E),o.l.info("Org height: "+E.height)}r.db.getRelations().forEach((function(t){o.l.info("tjoho"+p(t.id1)+p(t.id2)+JSON.stringify(t)),y.setEdge(p(t.id1),p(t.id2),{relation:t},t.title||"DEFAULT")})),r.db.getNotes().forEach((function(t){o.l.debug("Adding note: ".concat(JSON.stringify(t)));var e=s.s.drawNote(x,t,c,r);l[e.id]=e,y.setNode(e.id,e),t.class&&t.class in v&&y.setEdge(t.id,p(t.class),{relation:{id1:t.id,id2:t.class,relation:{type1:"none",type2:"none",lineType:10}}},"DEFAULT")})),(0,n.bK)(y),y.nodes().forEach((function(t){void 0!==t&&void 0!==y.node(t)&&(o.l.debug("Node "+t+": "+JSON.stringify(y.node(t))),f.select("#"+(r.db.lookUpDomId(t)||t)).attr("transform","translate("+(y.node(t).x-y.node(t).width/2)+","+(y.node(t).y-y.node(t).height/2)+" )"))})),y.edges().forEach((function(t){void 0!==t&&void 0!==y.edge(t)&&(o.l.debug("Edge "+t.v+" -> "+t.w+": "+JSON.stringify(y.edge(t))),s.s.drawEdge(x,y.edge(t),y.edge(t).relation,c,r))}));var L=x.node().getBBox(),M=L.width+40,N=L.height+40;(0,o.i)(x,N,M,c.useMaxWidth);var T="".concat(L.x-20," ").concat(L.y-20," ").concat(M," ").concat(N);o.l.debug("viewBox ".concat(T)),x.attr("viewBox",T)}},g={parser:r.p,db:r.d,renderer:c,styles:r.s,init:function(t){t.class||(t.class={}),t.class.arrowMarkerAbsolute=t.arrowMarkerAbsolute,r.d.clear()}}},4855:function(t,e,a){a.d(e,{p:function(){return o},s:function(){return p}});var r=a(8225),i=a(366),n=0,d=function(t){var e=t.id;return t.type&&(e+="<"+t.type+">"),e},o=function(t){var e="",a="",r="",n="",d=t.substring(0,1),o=t.substring(t.length-1,t.length);d.match(/[#+~-]/)&&(n=d);var s=/[\s\w)~]/;o.match(s)||(a=l(o));var p=""===n?0:1,c=""===a?t.length:t.length-1,g=(t=t.substring(p,c)).indexOf("("),h=t.indexOf(")");if(g>1&&h>g&&h<=t.length){var u=t.substring(0,g).trim(),f=t.substring(g+1,h);if(e=n+u+"("+(0,i.x)(f.trim())+")",h<t.length){var x=t.substring(h+1,h+2);""!==a||x.match(s)?r=t.substring(h+1).trim():(a=l(x),r=t.substring(h+2).trim()),""!==r&&(":"===r.charAt(0)&&(r=r.substring(1).trim()),e+=r=" : "+(0,i.x)(r))}}else e=n+(0,i.x)(t);return{displayText:e,cssStyle:a}},s=function(t,e,a,r){var i=o(e),n=t.append("tspan").attr("x",r.padding).text(i.displayText);""!==i.cssStyle&&n.attr("style",i.cssStyle),a||n.attr("dy",r.textHeight)},l=function(t){switch(t){case"*":return"font-style:italic;";case"$":return"text-decoration:underline;";default:return""}},p={getClassTitleString:d,drawClass:function(t,e,a,r){i.l.debug("Rendering class ",e,a);var n,o=e.id,l={id:o,label:e.id,width:0,height:0},p=t.append("g").attr("id",r.db.lookUpDomId(o)).attr("class","classGroup");n=e.link?p.append("svg:a").attr("xlink:href",e.link).attr("target",e.linkTarget).append("text").attr("y",a.textHeight+a.padding).attr("x",0):p.append("text").attr("y",a.textHeight+a.padding).attr("x",0);var c=!0;e.annotations.forEach((function(t){var e=n.append("tspan").text("\xab"+t+"\xbb");c||e.attr("dy",a.textHeight),c=!1}));var g=d(e),h=n.append("tspan").text(g).attr("class","title");c||h.attr("dy",a.textHeight);var u=n.node().getBBox().height,f=p.append("line").attr("x1",0).attr("y1",a.padding+u+a.dividerMargin/2).attr("y2",a.padding+u+a.dividerMargin/2),x=p.append("text").attr("x",a.padding).attr("y",u+a.dividerMargin+a.textHeight).attr("fill","white").attr("class","classText");c=!0,e.members.forEach((function(t){s(x,t,c,a),c=!1}));var y=x.node().getBBox(),v=p.append("line").attr("x1",0).attr("y1",a.padding+u+a.dividerMargin+y.height).attr("y2",a.padding+u+a.dividerMargin+y.height),b=p.append("text").attr("x",a.padding).attr("y",u+2*a.dividerMargin+y.height+a.textHeight).attr("fill","white").attr("class","classText");c=!0,e.methods.forEach((function(t){s(b,t,c,a),c=!1}));var m=p.node().getBBox(),w=" ";e.cssClasses.length>0&&(w+=e.cssClasses.join(" "));var k=p.insert("rect",":first-child").attr("x",0).attr("y",0).attr("width",m.width+2*a.padding).attr("height",m.height+a.padding+.5*a.dividerMargin).attr("class",w).node().getBBox().width;return n.node().childNodes.forEach((function(t){t.setAttribute("x",(k-t.getBBox().width)/2)})),e.tooltip&&n.insert("title").text(e.tooltip),f.attr("x2",k),v.attr("x2",k),l.width=k,l.height=m.height+a.padding+.5*a.dividerMargin,l},drawEdge:function(t,e,a,d,o){var s=function(t){switch(t){case o.db.relationType.AGGREGATION:return"aggregation";case o.db.relationType.EXTENSION:return"extension";case o.db.relationType.COMPOSITION:return"composition";case o.db.relationType.DEPENDENCY:return"dependency";case o.db.relationType.LOLLIPOP:return"lollipop"}};e.points=e.points.filter((function(t){return!Number.isNaN(t.y)}));var l,p,c=e.points,g=(0,r.jvg)().x((function(t){return t.x})).y((function(t){return t.y})).curve(r.$0Z),h=t.append("path").attr("d",g(c)).attr("id","edge"+n).attr("class","relation"),u="";d.arrowMarkerAbsolute&&(u=(u=(u=window.location.protocol+"//"+window.location.host+window.location.pathname+window.location.search).replace(/\(/g,"\\(")).replace(/\)/g,"\\)")),1==a.relation.lineType&&h.attr("class","relation dashed-line"),10==a.relation.lineType&&h.attr("class","relation dotted-line"),"none"!==a.relation.type1&&h.attr("marker-start","url("+u+"#"+s(a.relation.type1)+"Start)"),"none"!==a.relation.type2&&h.attr("marker-end","url("+u+"#"+s(a.relation.type2)+"End)");var f,x,y,v,b=e.points.length,m=i.u.calcLabelPosition(e.points);if(l=m.x,p=m.y,b%2!==0&&b>1){var w=i.u.calcCardinalityPosition("none"!==a.relation.type1,e.points,e.points[0]),k=i.u.calcCardinalityPosition("none"!==a.relation.type2,e.points,e.points[b-1]);i.l.debug("cardinality_1_point "+JSON.stringify(w)),i.l.debug("cardinality_2_point "+JSON.stringify(k)),f=w.x,x=w.y,y=k.x,v=k.y}if(void 0!==a.title){var E=t.append("g").attr("class","classLabel"),L=E.append("text").attr("class","label").attr("x",l).attr("y",p).attr("fill","red").attr("text-anchor","middle").text(a.title);window.label=L;var M=L.node().getBBox();E.insert("rect",":first-child").attr("class","box").attr("x",M.x-d.padding/2).attr("y",M.y-d.padding/2).attr("width",M.width+d.padding).attr("height",M.height+d.padding)}(i.l.info("Rendering relation "+JSON.stringify(a)),void 0!==a.relationTitle1&&"none"!==a.relationTitle1)&&t.append("g").attr("class","cardinality").append("text").attr("class","type1").attr("x",f).attr("y",x).attr("fill","black").attr("font-size","6").text(a.relationTitle1);void 0!==a.relationTitle2&&"none"!==a.relationTitle2&&t.append("g").attr("class","cardinality").append("text").attr("class","type2").attr("x",y).attr("y",v).attr("fill","black").attr("font-size","6").text(a.relationTitle2);n++},drawNote:function(t,e,a,r){i.l.debug("Rendering note ",e,a);var n=e.id,d={id:n,text:e.text,width:0,height:0},o=t.append("g").attr("id",n).attr("class","classGroup"),s=o.append("text").attr("y",a.textHeight+a.padding).attr("x",0),l=JSON.parse('"'.concat(e.text,'"')).split("\n");l.forEach((function(t){i.l.debug("Adding line: ".concat(t)),s.append("tspan").text(t).attr("class","title").attr("dy",a.textHeight)}));var p=o.node().getBBox(),c=o.insert("rect",":first-child").attr("x",0).attr("y",0).attr("width",p.width+2*a.padding).attr("height",p.height+l.length*a.textHeight+a.padding+.5*a.dividerMargin).node().getBBox().width;return s.node().childNodes.forEach((function(t){t.setAttribute("x",(c-t.getBBox().width)/2)})),d.width=c,d.height=p.height+l.length*a.textHeight+a.padding+.5*a.dividerMargin,d},parseMember:o}}}]);
//# sourceMappingURL=984.1fd8821b.chunk.js.map