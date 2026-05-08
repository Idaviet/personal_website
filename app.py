import matplotlib
matplotlib.use('Agg')  # Non-GUI backend — MUST be before any matplotlib imports

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
import sys

# Add the epitope src folder to path
sys.path.insert(0, '/Users/isaac_daviet/Desktop/coding/epitope_visualization/src')

from epitope_functions import (
    generate_epi_df,
    aggregate_plot_df,
    color_epitope_plot_by_property,
    plot_max_normalized_property,
    plot_all_physical_props,
    plot_antigen_property_distribution
)

app = Flask(__name__)
CORS(app)

PROPERTIES_TABLE = '/Users/isaac_daviet/Desktop/coding/epitope_visualization/aa_physicochemical_properties.csv'
PROP_COLS = [
    'hydrophobicity', 'hydrophilicity', 'h-bonds', 'side_chain_vol',
    'polarity', 'polarizability', 'solv_accessible_surface_area',
    'net_charge_index', 'aa_mass'
]

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    start_pos = request.form.get('start_pos', type=int)
    end_pos = request.form.get('end_pos', type=int)
    ag_seq = request.form.get('ag_seq', '')
    
    temp_path = '/tmp/uploaded_epitopes.csv'
    file.save(temp_path)
    
    try:
        # Run core pipeline
        epi_df = generate_epi_df(temp_path, start_pos, end_pos)
        plot_df = aggregate_plot_df(epi_df)
        
        # Property coloring
        res_props_df = plot_all_physical_props(
            plot_df, properties_table=PROPERTIES_TABLE
        )
        hold_df = plot_max_normalized_property(res_props_df, PROP_COLS)
        
        # Antigen property distribution
        antigen_result = None
        if ag_seq:
            antigen_result = plot_antigen_property_distribution(
                plot_df, ag_seq, PROP_COLS, PROPERTIES_TABLE
            )
        
        result = {
            'epi_df': epi_df.reset_index().to_dict(orient='records'),
            'plot_df': plot_df.to_dict(orient='records'),
            'res_props_df': res_props_df.to_dict(orient='records'),
            'hold_df': hold_df.to_dict(orient='records'),
            'summary': {
                'total_positions': len(plot_df),
                'total_epitopes': int(epi_df['count'].sum()) if 'count' in epi_df.columns else len(epi_df),
                'start_pos': start_pos,
                'end_pos': end_pos
            }
        }
        
        if antigen_result is not None:
            result['antigen_df'] = antigen_result.to_dict(orient='records')
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
