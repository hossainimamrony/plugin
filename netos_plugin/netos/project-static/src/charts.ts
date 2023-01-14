export interface Point {
  x: number | string;
  y: number | string;
}

export interface Serie {
  name: string;
  data: Point[] | number[];
}

export const barChart = (categories: string[], values: number[], title: string, events = {}) => {

  const options = {
    series: [
      {
        data: values
      }
    ],
    chart: {
      type: 'bar',
      height: 350,
      events: events
    },
    title: {
      text: title,
      align: 'left',
      margin: 10,
      offsetX: 0,
      offsetY: 0,
      floating: false,
      style: {
        fontSize: '16px',
        fontWeight: 'bold',
        color: 'inherit'
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: categories,
    },
    yaxis: {
      title: {
        text: 'Count'
      },
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val: string) {
          return val
        }
      }
    }
  };

  return options

}


export const pieChart = (categories: string[], values: number[], title: string, events: any = {}) => {
  const options = {
    series: values,
    chart: {
      width: 380,
      type: 'pie',
      events: events
    },
    title: {
      text: title,
      align: 'left',
      margin: 10,
      offsetX: 0,
      offsetY: 0,
      floating: false,
      style: {
        fontSize: '16px',
        fontWeight: 'bold',
        color: 'inherit'
      },
    },
    legend: {
      position: 'bottom',
    },
    labels: categories,
    responsive: [
      {
        breakpoint: 1441,
        options: {
          chart: {
            width: 280,
          },
          legend: {
            position: 'bottom',
          }
        },
      }]
  };

  return options;
}


export const heatChart = (series: Serie[], title: string, events: any = {}) => {
  const options = {
    series: series,
    title: {
      text: title,
      align: 'left',
      margin: 10,
      offsetX: 0,
      offsetY: 0,
      floating: false,
      style: {
        fontSize: '16px',
        fontWeight: 'bold',
        color: 'inherit'
      },
    },
    chart: {
      height: 350,
      events: events,
      type: 'heatmap',
    },
    dataLabels: {
      enabled: false
    },
    plotOptions: {
      heatmap: {
        colorScale: {
          ranges: [{
            from: 0,
            to: 5,
            color: '#00A100',
            name: 'low',
          },
          {
            from: 6,
            to: 25,
            color: '#128FD9',
            name: 'medium',
          },
          {
            from: 26,
            to: 60,
            color: '#FFB200',
            name: 'high',
          }
          ]
        }
      }
    }
  };

  return options;

}

export const stackedBar = (categories: string[], series: Serie[], title: string, events: any = {}) => {
  const options = {
    title: {
      text: title,
      align: 'left',
      margin: 10,
      offsetX: 0,
      offsetY: 0,
      floating: false,
      style: {
        fontSize: '16px',
        fontWeight: 'bold',
        color: 'inherit'
      },
    },
    series: series,
    chart: {
      type: 'bar',
      height: 350,
      stacked: true,
      events: events,
      stackType: '100%'
    },
    plotOptions: {
      bar: {
        horizontal: true,
      },
    },
    stroke: {
      width: 1,
      colors: ['#fff']
    },
    xaxis: {
      categories: categories,
    },
    tooltip: {
    },
    fill: {
      opacity: 1

    },
    legend: {
      position: 'top',
      horizontalAlign: 'left',
      offsetX: 40
    }
  }

  return options;
}
