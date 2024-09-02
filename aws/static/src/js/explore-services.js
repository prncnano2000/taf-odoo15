import publicWidget from "web.public.widget";

publicWidget.registry.AwsServices = publicWidget.Widget.extend({
    selector: ".explore-services",

    start() {
        let servicesRow = this.el.querySelector("#yh-services-row")
        if (servicesRow){
            this._rpc({
                route: "/services/",
                params:{}
            }).then(data=>{
                let html = ""
                data.forEach(services=>{
                    html +=`<div class="col-lg-3 mb-5">
                                <div class="d-flex align-items-center">
                                    <div class="img-container mr-3 rounded">
                                        <img class="country-image rounded" src="data:image/png;base64,${services.image}"/>
                                    </div>
                                    <div>
                                        <h2 class="mb-0">${services.name ? services.name[1] : ""}</h2>
                                        <div>${services.description ? services.description[1] : ""}</div>
                                    </div>
                                </div>
                            </div>`
                })
                servicesRow.innerHTML = html
            })
        }
    },

});

export default publicWidget.registry.AwsServices;