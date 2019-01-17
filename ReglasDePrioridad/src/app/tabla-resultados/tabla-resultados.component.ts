import { Component, OnInit, NgZone } from '@angular/core';
import { APIService } from '../api.service';
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import { ActivatedRoute } from '@angular/router';
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
am4core.useTheme(am4themes_animated);
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
   idEjecucion: number;
  private faseBuena: Array<object> = [];
  constructor(private apiService: APIService, private zone: NgZone,  private route: ActivatedRoute ) { }
  
  ngOnInit() {
    this.idEjecucion = +this.route.snapshot.paramMap.get('id'),
    console.log(this.idEjecucion),
    //console.log(id);
    this.getResultados(),
    console.log(this.fase)
    
    
  }
  getResultados(){
    
    this.apiService.getPiezaResultado(this.idEjecucion).subscribe((data: Array<object>) => {
      
      this.resultadoPiezas = data;
      console.log(data);
    });
  this.apiService.getTablaResultados(this.idEjecucion).subscribe((data: Array<object>) => {
    
    this.resultado = [data];
    console.log(data);
  });
  this.apiService.getEjecucionFases(this.idEjecucion).subscribe((data: Array<object>) => {
      
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
  this.zone.runOutsideAngular(() => {
  let chart = am4core.create("chartdiv", am4charts.XYChart);
chart.hiddenState.properties.opacity = 0; // this creates initial fade-in
//chart.responsive.enabled = true;
//chart.paddingRight = 190;
chart.paddingLeft = 0;
chart.height=400;
chart.dateFormatter.inputDateFormat = "yyyy-MM-dd HH:mm";

let colorSet = new am4core.ColorSet();
colorSet.saturation = 0.4;
for(let item of this.fase){
  let vara = {
    id: item['id'],
    nPieza: item['nPieza'],
    nPiezaEje: item['nPiezaEje'],
    ejecucion: item['ejecucion'],
    maquinaText:  " C.T " +item['maquinaNecesaria'],
    nFase: item['nFase']+1,
    tiempoRequerido: item['tiempoRequerido'],
    maquinaNecesaria: item['maquinaNecesaria'],
    tiempoFaseEntrada: item['tiempoFaseEntrada'],
    tiempoFaseSalida: item['tiempoFaseSalida'],
    color :  colorSet.getIndex(item['color']).brighten(item['brightness'])};
  this.faseBuena.push(vara);
}
console.log(this.faseBuena)


chart.data=this.faseBuena;
console.log(chart.data);


let categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
categoryAxis.tooltipText= "C.T. ";

categoryAxis.dataFields.category = "maquinaText";
categoryAxis.renderer.grid.template.location = 0;
categoryAxis.renderer.inversed = true;
//categoryAxis.renderer.labels.template.fill = am4core.color("#black");
let valueAxis = chart.xAxes.push(new am4charts.ValueAxis());
valueAxis.min=0;
valueAxis.max=12;
valueAxis.renderer.tooltipLocation = 0;
valueAxis.title.text="Unidades de tiempo";
/*let DurationAxis = chart.xAxes.push(new am4charts.DateAxis());
DurationAxis.title.text="Time";
DurationAxis.min=0;
DurationAxis.max=20;*/
let series1 = chart.series.push(new am4charts.ColumnSeries());
series1.columns.template.width = am4core.percent(80);
series1.columns.template.tooltipText = "Número de Pieza {nPiezaEje} - Número de Fase {nFase} - C.T {maquinaNecesaria} - Tiempor Requerido {tiempoRequerido}";
//series1.dataFields.valueX=2;
//series1.dataFields.categoryY = "nFase";
series1.dataFields.openValueX="tiempoFaseEntrada";
series1.dataFields.valueX = "tiempoFaseSalida";
series1.dataFields.categoryY = "maquinaText";
series1.columns.template.propertyFields.fill = "color"; // get color from data
series1.columns.template.propertyFields.stroke = "color";


series1.columns.template.strokeOpacity = 1;

chart.scrollbarX = new am4core.Scrollbar();
  });
}
}
