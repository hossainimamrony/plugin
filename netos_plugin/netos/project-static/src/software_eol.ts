import { Serie, stackedBar } from "./charts";
import ApexCharts from 'apexcharts'

interface SoftwareEolData {
    vendor: string;
    vulnerability_date: string;
    last_day_of_support_date: number;
    maintenance_date: number;
    last_sale_date: number;
    vendor_id: number;
}

enum ChartType {
    SiteChart = 'site',
    RegionChart = 'region',
    DeviceTypeChart = 'device_type',
    DeviceRoleChart = 'role',
    VendorChart = 'manufacturer',
}


function parseModelData(data: HTMLElement): SoftwareEolData[] {
    const m = [];

    for (const child of data.children) {
        const data = child.innerHTML.split(";")
        let d_dict: any = {};

        for (let d of data) {
            let [name, value] = d.split(",")
            d_dict[name] = value;

        }
        m.push(d_dict);

    }
    return m as SoftwareEolData[];
}
function generateCharts(rootNode: Element, data: SoftwareEolData[], type: ChartType) {
    let catg = [];
    let values: any = {};
    let title = "Vendor Software EoL";

    values["last_day_of_support_date"] = [];
    values["last_sale_date"] = [];
    values["maintenance_date"] = [];
    values["vulnerability_date"] = [];

    // Site chart
    if (data.length > 0) {

        for (let d of data) {    
            values["last_day_of_support_date"].push(d.last_day_of_support_date);
            values["last_sale_date"].push(d.last_sale_date);
            values["maintenance_date"].push(d.maintenance_date);
            values["vulnerability_date"].push(d.vulnerability_date);
            catg.push(d.vendor)
        }

        let series: Serie[] = [
            {
                name: "last day of support date",
                data: values["last_day_of_support_date"]
            },
            {
                name: "last sale date",
                data: values["last_sale_date"]
            },
            {
                name: "maintenance date",
                data: values["maintenance_date"]
            },
            {
                name: "vulnerability date",
                data: values["vulnerability_date"]
            },
        ]

        catg = catg.map(el => el.replace('_', ' '));

        const events = {
            dataPointSelection: function (event: any, chartContext: any, config: any) {
    
                let y = config.dataPointIndex;

                const params = new URLSearchParams();
                const vendor_id = data[y].vendor_id;
        
                if (vendor_id) {
                    params.set("manufacturer_id", String(vendor_id))
                    location.search = params.toString();
                } else {
                    console.error("Invalid vendor id");
                }
            }
        }
        
        const options = stackedBar(catg, series, title, events);
        const el = document.createElement("div");
        el.classList.add('col-lg-6', 'col-md-10', 'col-12', 'col');

        const childEl = document.createElement('div');
        childEl.classList.add('card', 'mx-1');
        el.appendChild(childEl);

        const chartEl = new ApexCharts(childEl, options);
        rootNode.appendChild(el);
        chartEl.render();

    } else {
        const el = document.createElement("div");
        const elSpan = document.createElement("span")
        elSpan.innerHTML = "No data to generate reports";
        el.appendChild(elSpan);
        rootNode.appendChild(el);
    }
}

function updateCharts() {
    const siteData = document.querySelector<HTMLElement>("#eol-data");

    const siteRoot = document.querySelector("#eol-chart-list");

    // Charts data
    const siteMap = parseModelData(siteData);


    // Site chart
    generateCharts(siteRoot, siteMap, ChartType.SiteChart);


}

function init() {
    updateCharts();
}

init();
