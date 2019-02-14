import { Component, OnInit, NgZone } from '@angular/core';
import { APIService } from '../api.service';
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import { ActivatedRoute } from '@angular/router';
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import { element } from '@angular/core/src/render3/instructions';
am4core.useTheme(am4themes_animated);
//import am4themes_themes/kelly.js from "@amcharts/amcharts4/themes/themes/kelly.js";
@Component({
  selector: 'app-tabla-resultados',
  templateUrl: './tabla-resultados.component.html',
  styleUrls: ['./tabla-resultados.component.css']
})
export class TablaResultadosComponent implements OnInit {
  resultado: Array<object> = [];
  resultadoPiezas: Array<object> = [];
  fase: Array<object> = [];
  idEjecucion: number;
  resultadoCapas = [];
  idGra = 0;
  faseBuena: Array<object> = [];
  constructor(private apiService: APIService, private zone: NgZone, private route: ActivatedRoute) { }

  ngOnInit() {
    this.idEjecucion = +this.route.snapshot.paramMap.get('id'),
      console.log(this.idEjecucion),
      //console.log(id);
      this.getResultados(),
      console.log(this.fase)


  }
  getResultados() {

    this.apiService.getPiezaResultado(this.idEjecucion).subscribe((data: Array<object>) => {
      let ejecucion = [];
      var i = 0;
      for (let elemento of data) {
        let indiceCriba = elemento['indiceResultado']
        console.log(indiceCriba);
        if (i < indiceCriba) {
          i += 1;
          this.resultadoCapas.push(ejecucion);
          ejecucion = [];
          console.log("AAAAAAAAAAAAAAA")
        }
        ejecucion.push(elemento);
        console.log(elemento)
      }
      this.resultadoCapas.push(ejecucion);
      console.log(this.resultadoCapas)

      this.resultadoPiezas = data;
      this.getEjeFase()
      console.log(data);
    });
    this.apiService.getTablaResultados(this.idEjecucion).subscribe((data: Array<object>) => {

      this.resultado = data;
      console.log(data);
    });


    /* Chart code */
    // Themes begin
    //am4core.useTheme(am4themes_kelly);
    //am4core.useTheme(am4themes_animated);
    // Themes end
    return this.fase;

  }

  getEjeFase() {

    this.apiService.getEjecucionFases(this.idEjecucion).subscribe((data: Array<object>) => {
      var i = 0;
      let indiceCriba: number = 0;
      let element;
      let ejecucion = [];
      for (let elemento of data) {
        element = elemento;
        indiceCriba = elemento['indiceResultado']

        let ejecucion2 = ejecucion;
        this.fase = ejecucion;
        console.log(elemento);
        if (i < indiceCriba) {
          this.idGra = i;
          //this.fase = ejecucion2;
          this.creaGrafico(this.fase);
          this.faseBuena = [];
          console.log(this.fase);

          console.log(ejecucion2)
          ejecucion = [];
          ejecucion2 = [];
          this.fase = [];
          console.log(this.idGra)
          console.log(i)
          i += 1;
        }
        this.fase.push(elemento)

      }

      console.log(this.idGra = i);



      this.creaGrafico(this.fase);
      console.log(this.fase);

    });
  }





  creaGrafico(fase) {
    console.log(fase);
    this.zone.runOutsideAngular(() => {
      let chart = am4core.create(String(this.idGra), am4charts.XYChart);

      chart.hiddenState.properties.opacity = 0; // this creates initial fade-in
      //chart.responsive.enabled = true;
      //chart.paddingRight = 190;
      chart.paddingLeft = 0;
      chart.height = 400;
      chart.dateFormatter.inputDateFormat = "yyyy-MM-dd HH:mm";

      let colorSet = new am4core.ColorSet();
      colorSet.saturation = 0.4;
      console.log(this.fase)
      var tiempoMax = 0;
      for (let item of this.fase) {
        let vara = {
          id: item['id'],
          nPieza: item['nPieza'],
          nPiezaEje: item['nPiezaEje'],
          ejecucion: item['ejecucion'],
          maquinaText: " C.T " + item['maquinaNecesaria'],
          nFase: item['nFase'] + 1,
          tiempoRequerido: item['tiempoRequerido'],
          maquinaNecesaria: item['maquinaNecesaria'],
          tiempoFaseEntrada: item['tiempoFaseEntrada'],
          tiempoFaseSalida: item['tiempoFaseSalida'],
          color: colorSet.getIndex(item['color']).brighten(item['brightness'])
        };
        tiempoMax=item['tiempoMax'];
        this.faseBuena.push(vara);
      }
      console.log(this.faseBuena)


      chart.data = this.faseBuena;
      console.log(chart.data);


      let categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
      categoryAxis.tooltipText = "C.T. ";

      categoryAxis.dataFields.category = "maquinaText";
      categoryAxis.renderer.grid.template.location = 0;
      categoryAxis.renderer.inversed = true;
      //categoryAxis.renderer.labels.template.fill = am4core.color("#black");
      let valueAxis = chart.xAxes.push(new am4charts.ValueAxis());
      valueAxis.min = 0;
      valueAxis.max = tiempoMax;
      valueAxis.renderer.tooltipLocation = 0;
      valueAxis.title.text = "Unidades de tiempo";
      /*let DurationAxis = chart.xAxes.push(new am4charts.DateAxis());
      DurationAxis.title.text="Time";
      DurationAxis.min=0;
      DurationAxis.max=20;*/
      let series1 = chart.series.push(new am4charts.ColumnSeries());
      series1.columns.template.width = am4core.percent(80);
      series1.columns.template.tooltipText = "Número de Pieza {nPiezaEje} - Número de Fase {nFase} - C.T {maquinaNecesaria} - Tiempor Requerido {tiempoRequerido}";

      //series1.columns.template.textDecoration="Número de Pieza {nPiezaEje} - Número de Fase {nFase} - C.T {maquinaNecesaria} - Tiempor Requerido {tiempoRequerido}";
      //series1.itemReaderText="Número de Pieza {nPiezaEje} - Número de Fase {nFase} - C.T {maquinaNecesaria} - Tiempor Requerido {tiempoRequerido}";

      //series1.dataFields.valueX=2;
      //series1.dataFields.categoryY = "nFase";
      series1.dataFields.openValueX = "tiempoFaseEntrada";
      series1.dataFields.valueX = "tiempoFaseSalida";
      series1.dataFields.categoryY = "maquinaText";
      series1.columns.template.propertyFields.fill = "color"; // get color from data
      series1.columns.template.propertyFields.stroke = "color";
      let bullet1 = series1.bullets.push(new am4charts.LabelBullet());
      //bullet1.label.text="{nPiezaEje} - {nFase} -{maquinaNecesaria} - {tiempoRequerido}";
      /*let label = series1.columns.template.createChild(am4core.Label);
      label.text = "{nPiezaEje}-{nFase}-{maquinaNecesaria}-{tiempoRequerido}";
      label.fontWeight="bolder";
      label.align="center";*/
      //label.fontFamily.fontcolor("000000");
      //label.fontSize="xl";
      series1.columns.template.strokeOpacity = 1;

      chart.scrollbarX = new am4core.Scrollbar();
    });

  }
}
