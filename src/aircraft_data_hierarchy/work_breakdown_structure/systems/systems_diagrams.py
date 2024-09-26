import graphviz
from tabulate import tabulate
from typing import List, Optional
from IPython.display import display, Image, HTML
from .systems import System

def create_system_diagram(system: System) -> graphviz.Digraph:
    dot = graphviz.Digraph(comment=f'Functional Block Diagram - {system.name}')
    dot.attr(rankdir='LR', size='14,10', ratio='fill')

    for block in system.attributes.functional_blocks:
        dot.node(block.block_id, block.name, shape='box', style='filled', fillcolor='lightblue')

    for signal in system.attributes.data_signals:
        dot.edge(signal.source, signal.destination, label=signal.name, fontsize='8', len='1.5')

    return dot

def create_system_attribute_tables(system: System) -> List[str]:
    tables = []

    # Physical Characteristics
    phys_char = system.attributes.physical_characteristics
    tables.append(("Physical Characteristics", [
        ["Attribute", "Value", "Unit"],
        ["Weight", f"{phys_char.weight:.2f}", "kg"],
        ["Length", f"{phys_char.dimensions['length']:.3f}", "m"],
        ["Width", f"{phys_char.dimensions['width']:.3f}", "m"],
        ["Height", f"{phys_char.dimensions['height']:.3f}", "m"],
        ["Volume", f"{phys_char.volume:.3f}", "m³"],
        ["Center of Gravity X", f"{phys_char.center_of_gravity['x']:.3f}", "m"],
        ["Center of Gravity Y", f"{phys_char.center_of_gravity['y']:.3f}", "m"],
        ["Center of Gravity Z", f"{phys_char.center_of_gravity['z']:.3f}", "m"]
    ]))

    # Cooling Requirements
    cooling = system.attributes.cooling_requirements
    tables.append(("Cooling Requirements", [
        ["Attribute", "Value", "Unit"],
        ["Method", cooling.method, "N/A"],
        ["Heat Dissipation", f"{cooling.heat_dissipation:.1f}", "W"],
        ["Max Operating Temperature", f"{cooling.max_operating_temperature:.1f}", "°C"]
    ]))

    # Power Requirements
    power = system.attributes.power_requirements
    tables.append(("Power Requirements", [
        ["Attribute", "Value", "Unit"],
        ["Voltage", f"{power.voltage:.1f}", "V"],
        ["Current", f"{power.current:.2f}", "A"],
        ["Frequency", f"{power.frequency:.1f}" if power.frequency else "N/A", "Hz"],
        ["Power Type", power.power_type, "N/A"],
        ["Peak Power", f"{power.peak_power:.1f}", "W"],
        ["Average Power", f"{power.average_power:.1f}", "W"]
    ]))

    # Fluid Flow Characteristics
    if system.attributes.fluid_flow:
        fluid = system.attributes.fluid_flow
        tables.append(("Fluid Flow Characteristics", [
            ["Attribute", "Value", "Unit"],
            ["Fluid Type", fluid.fluid_type, "N/A"],
            ["Flow Rate", f"{fluid.flow_rate:.2f}", "L/min"],
            ["Max Pressure", f"{fluid.max_pressure/1e3:.2f}", "kPa"],
            ["Min Pressure", f"{fluid.min_pressure/1e3:.2f}", "kPa"],
            ["Min Temperature", f"{fluid.temperature_range[0]:.1f}", "°C"],
            ["Max Temperature", f"{fluid.temperature_range[1]:.1f}", "°C"],
            ["Viscosity", f"{fluid.viscosity:.6f}", "Pa·s"],
            ["Density", f"{fluid.density:.1f}", "kg/m³"]
        ]))

    return [(title, tabulate(data, headers="firstrow", tablefmt="html")) for title, data in tables]

def display_system_info(system: System):
    # Create and display the system diagram
    diagram = create_system_diagram(system)
    diagram.render("system_diagram", format="png", cleanup=True)
    display(Image("system_diagram.png"))

    # Create attribute tables
    tables = create_system_attribute_tables(system)

    # Display tables side by side
    html_tables = "<table><tr>" + "".join([f"<td style='vertical-align:top'><h4>{title}</h4>{table}</td>" for title, table in tables]) + "</tr></table>"
    display(HTML(html_tables))
    
