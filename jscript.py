from st_aggrid import JsCode

cellRenderer_addButton = JsCode('''
    class BtnCellRenderer {
        init(params) {
            this.params = params;
            this.eGui = document.createElement('div');
            this.eGui.innerHTML = `
            <span>
                <style>
                .btn_add {
                    background-color: #71DC87;
                    border: 2px solid black;
                    color: #D05732;
                    text-align: center;
                    display: inline-block;
                    font-size: 12px;
                    font-weight: bold;
                    height: 2em;
                    width: 10em;
                    border-radius: 12px;
                    padding: 0px;
                }
                </style>
                <button id='click-button' 
                    class="btn_add" 
                    > Add</button>
            </span>
        `;
        }

        getGui() {
            return this.eGui;
        }

    };
    ''')

cellRenderer_removeButton = JsCode('''
    class BtnCellRenderer {
        init(params) {
            this.params = params;
            this.eGui = document.createElement('div');
            this.eGui.innerHTML = `
            <span>
                <style>
                .btn_add {
                    background-color: #71DC87;
                    border: 2px solid black;
                    color: #D05732;
                    text-align: center;
                    display: inline-block;
                    font-size: 12px;
                    font-weight: bold;
                    height: 2em;
                    width: 10em;
                    border-radius: 12px;
                    padding: 0px;
                }
                </style>
                <button id='click-button' 
                    class="btn_add" 
                    > Delete</button>
            </span>
        `;
        }

        getGui() {
            return this.eGui;
        }

    };
    ''')

js_add_row = JsCode("""
function(e) {
    let api = e.api;
    let rowPos = e.rowIndex + 1; 
    api.applyTransaction({addIndex: rowPos, add: [{}]})    
};
"""
)

js_remove_row = JsCode("""
function(e) {
    let api = e.api;
    let sel = api.getSelectedRows();
    api.applyTransaction({remove: sel})    
};
"""
)
