import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
//import am4themes_themes/kelly.js from "@amcharts/amcharts4/themes/themes/kelly.js";
@Component({
  selector: 'app-tabla-resultados',
  templateUrl: './tabla-resultados.component.html',
  styleUrls: ['./tabla-resultados.component.css']
})
export class TablaResultadosComponent implements OnInit {
  private resultado: Array<object> = [];
  private resultadoPiezas: Array<object> = [];
   fase: Array<object> = [];
  private faseBuena: Array<object> = [];
  private faseBuenad: Array<object> = [
    {
      
  
      maquinaNecesaria: 1,
      nFase: 2,
      nPieza: 3
      
    },{
      
  
      maquinaNecesaria: 1,
      nFase: 9,
      nPieza: 4
      
    },{
      
  
      maquinaNecesaria: 2,
      nFase: 4,
      nPieza: 5
    
    }];;
  constructor(private apiService: APIService) { }

  ngOnInit() {
    this.getResultados(),
    console.log(this.fase)
    
    
  }
  getResultados(){
    
    this.apiService.getPiezaResultado().subscribe((data: Array<object>) => {
      
      this.resultadoPiezas = data;
      console.log(data);
    });
  this.apiService.getTablaResultados().subscribe((data: Array<object>) => {
    
    this.resultado = [data];
    console.log(data);
  });
  this.apiService.getEjecucionFases().subscribe((data: Array<object>) => {
      
     this.fase = data;
    console.log(data);
    console.log(this.fase);
    this.creaGrafico(this.fase);
  
  });
  /* Chart code */
// Themes begin
//am4core.useTheme(am4themes_kelly);
//am4core.useTheme(am4themes_animated);
// Themes end
 return this.fase;

}

creaGrafico(fase){
  console.log(fase);
  let chart = am4core.create("chartdiv", am4charts.XYChart);
chart.hiddenState.properties.opacity = 0; // this creates initial fade-in

chart.paddingRight = 190;
chart.paddingLeft = 470;
chart.dateFormatter.inputDateFormat = "yyyy-MM-dd HH:mm";

let colorSet = new am4core.ColorSet();
colorSet.saturation = 0.4;
for(let item of this.fase){
  let vara = {
    id: item['id'],
    nPieza: item['nPieza'],
    ejecucion: item['ejecucion'],
    nFase: item['nFase'],
    tiempoRequerido: item['tiempoRequerido'],
    maquinaNecesaria: item['maquinaNecesaria'],
    tiempoFaseEntrada: item['tiempoFaseEntrada'],
    tiempoFaseSalida: item['tiempoFaseSalida'],
    color :  colorSet.getIndex(item['color']).brighten(item['brightness'])};
  this.faseBuena.push(vara);
}
console.log(this.faseBuena)
//chart.data=this.faseBuena;
/*chart.data = [
  {
    name: "John",
    fromDate: "2018-01-01 08:00",
    toDate: "2018-01-01 10:00",
    color: colorSet.getIndex(0).brighten(0)
  },
  {
    name: "John",
    fromDate: "2018-01-01 12:00",
    toDate: "2018-01-01 15:00",
    color: colorSet.getIndex(0).brighten(0.4)
  },
  {
    name: "John",
    fromDate: "2018-01-01 15:30",
    toDate: "2018-01-01 21:30",
    color: colorSet.getIndex(0).brighten(0.8)
  },

  {
    name: "Jane",
    fromDate: "2018-01-01 09:00",
    toDate: "2018-01-01 12:00",
    color: colorSet.getIndex(2).brighten(0)
  },
  {
    name: "Jane",
    fromDate: "2018-01-01 13:00",
    toDate: "2018-01-01 17:00",
    color: colorSet.getIndex(2).brighten(0.4)
  },

  {
    name: "Peter",
    fromDate: "2018-01-01 11:00",
    toDate: "2018-01-01 16:00",
    color: colorSet.getIndex(4).brighten(0)
  },
  {
    name: "Peter",
    fromDate: "2018-01-01 16:00",
    toDate: "2018-01-01 19:00",
    color: colorSet.getIndex(4).brighten(0.4)
  },

  {
    name: "Melania",
    fromDate: "2018-01-01 16:00",
    toDate: "2018-01-01 20:00",
    color: colorSet.getIndex(6).brighten(0)
  },
  {
    name: "Melania",
    fromDate: "2018-01-01 20:30",
    toDate: "2018-01-01 24:00",
    color: colorSet.getIndex(6).brighten(0.4)
  },

  {
    name: "Donald",
    fromDate: "2018-01-01 13:00",
    toDate: "2018-01-01 24:00",
    color: colorSet.getIndex(8).brighten(0)
  }
];*/
chart.data = [
  {
    id: 1, 
    nPieza: 16,
     ejecucion: 50, 
     nFase: 1,
    tiempoRequerido: 2.0, maquinaNecesaria: 1, tiempoFaseEntrada: 0.5, tiempoFaseSalida: 2.5}];/*,{
    

    maquinaNecesaria: 1,
    nFase: 9,
    nPieza: 4,
    color: colorSet.getIndex(5).brighten(0.3)
  },{
    

    maquinaNecesaria: 2,
    nFase: 4,
    nPieza: 5,
    color: colorSet.getIndex(0).brighten(0)
  }];*/
chart.data=this.faseBuena;
console.log(chart.data);


let categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "maquinaNecesaria";
categoryAxis.renderer.grid.template.location = 0;
categoryAxis.renderer.inversed = true;
//categoryAxis.renderer.labels.template.fill = am4core.color("#black");
let valueAxis = chart.xAxes.push(new am4charts.ValueAxis());
valueAxis.min=0;
valueAxis.max=10;
valueAxis.renderer.tooltipLocation = 0;
/*let DurationAxis = chart.xAxes.push(new am4charts.DateAxis());
DurationAxis.title.text="Time";
DurationAxis.min=0;
DurationAxis.max=20;*/
let series1 = chart.series.push(new am4charts.ColumnSeries());
series1.columns.template.width = am4core.percent(80);
series1.columns.template.tooltipText = "Número de Pieza{nPieza} Número de Fase {";
//series1.dataFields.valueX=2;
//series1.dataFields.categoryY = "nFase";
series1.dataFields.openValueX="tiempoFaseEntrada";
series1.dataFields.valueX = "tiempoFaseSalida";
series1.dataFields.categoryY = "maquinaNecesaria";
series1.columns.template.propertyFields.fill = "color"; // get color from data
series1.columns.template.propertyFields.stroke = "color";
/*let color =  colorSet.getIndex(5);
let fillModifier = new am4core.LinearGradientModifier();

fillModifier.brightnesses=[0.2];
fillModifier.opacities = [1, 1, 0];
fillModifier.offsets = [0, 1];
fillModifier.gradient.rotation = 0;

series1.columns.template.fillModifier=fillModifier;*/

series1.columns.template.strokeOpacity = 1;
//series1.columns.template.propertyFields.stroke =  am4core.color("#3787ac");
chart.scrollbarX = new am4core.Scrollbar();
}
}
