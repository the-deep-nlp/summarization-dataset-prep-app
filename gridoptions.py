from st_aggrid import GridOptionsBuilder

from jscript import (
    js_add_row,
    js_remove_row,
    cellRenderer_addButton,
    cellRenderer_removeButton
)

gb = GridOptionsBuilder()
gb.configure_pagination(enabled=True)

gb.configure_column(
    field="abc",
    header_name="Analytical Statement",
    type=["string"],
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb.configure_column(
    field="xyz",
    header_name="Comparison with previous months",
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb.configure_column(
    field="efg",
    header_name="Evidence",
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb.configure_column(
    field="Add row",
    onCellClicked=js_add_row,
    cellRenderer=cellRenderer_addButton,
    lockPosition='right',
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb.configure_column(
    field="Delete row",
    onCellClicked=js_remove_row,
    cellRenderer=cellRenderer_removeButton,
    lockPosition='right',
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
    editable=True
)
gb.configure_selection(selection_mode="single", use_checkbox=True)
gb.configure_grid_options(stopEditingWhenCellsLoseFocus=True, headerHeight=50, rowHeight=30)
go = gb.build()


gb_dump = GridOptionsBuilder()
gb_dump.configure_pagination(enabled=True)
gb_dump.configure_column(
    field="anecdotal",
    header_name="Anecdotal",
    type=["string"],
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb_dump.configure_column(
    field="too_old",
    header_name="Too old",
    type=["string"],
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb_dump.configure_column(
    field="redundant",
    header_name="Redundant",
    type=["string"],
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb_dump.configure_column(
    field="outliers",
    header_name="Outliers",
    type=["string"],
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb_dump.configure_column(
    field="Add row",
    onCellClicked=js_add_row,
    cellRenderer=cellRenderer_addButton,
    lockPosition='right',
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb_dump.configure_column(
    field="Delete row",
    onCellClicked=js_remove_row,
    cellRenderer=cellRenderer_removeButton,
    lockPosition='right',
    wrapHeaderText=True,
    wrapText=True,
    autoHeight=True
)
gb_dump.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
    editable=True
)
gb_dump.configure_selection(selection_mode="single", use_checkbox=True)
gb_dump.configure_grid_options(stopEditingWhenCellsLoseFocus=True, headerHeight=50, rowHeight=30)
go_dump = gb_dump.build()
