import React from 'react';
import genBins, { Bin, Bins } from '@visx/mock-data/lib/generators/genBins';
import { scaleLinear } from '@visx/scale';
import { HeatmapRect } from '@visx/heatmap';
import { getSeededRandom } from '@visx/mock-data';

const cool1 = '#E5F6DF';
const cool2 = '#2B463C';


function max<Datum>(data: Datum[], value: (d: Datum) => number): number {
    return Math.max(...data.map(value));
}

export type HeatMapDataType = {bin: number, count: number}[]

export type HeatmapProps = {
    width: number;
    height: number;
    data: HeatMapDataType;
    margin?: { top: number; right: number; bottom: number; left: number };
    separation?: number;
    events?: boolean;
};

const defaultMargin = { top: 10, left: 20, right: 20, bottom: 110 };

const Example = ({
                     width,
                     height,
                     data,
                     events = false,
                     margin = defaultMargin,
                     separation = 20,
                 }: HeatmapProps) => {
    const bins = (d: Bins) => d.bins;
    const count = (d: Bin) => d.count;
    const seededRandom = getSeededRandom(0.41);
    const binData = genBins(
        /* length = */ 7,
        /* height = */ 32,
        /** binFunc */ (idx) => 150 * idx,
        /** countFunc */ (i, number) => 25 * (number - i) * seededRandom(),
    );
    const colorMax = max(binData, (d) => max(bins(d), count));
    const bucketSizeMax = max(binData, (d) => bins(d).length);

// scales
    const xScale = scaleLinear<number>({
        domain: [0, 12],
    });
    const yScale = scaleLinear<number>({
        domain: [0, bucketSizeMax],
    });
    const rectColorScale = scaleLinear<string>({
        range: [cool1, cool2],
        domain: [0, colorMax],
    });

    // bounds
    const size =
        width > margin.left + margin.right ? width - margin.left - margin.right - separation : width;
    const xMax = 200;
    const yMax = 500;

    const binWidth = 15;
    const binHeight = 15;

    xScale.range([0, xMax]);
    yScale.range([yMax, 0]);

    return width < 10 ? null : (
        <svg width={width} height={height}>
                <HeatmapRect
                    data={binData}
                    xScale={(d) => xScale(d) ?? 0}
                    yScale={(d) => yScale(d) ?? 0}
                    colorScale={rectColorScale}
                    binWidth={binWidth}
                    binHeight={binWidth}
                    gap={2}
                >
                    {(heatmap) =>
                        heatmap.map((heatmapBins) =>
                            heatmapBins.map((bin) => (
                                <rect
                                    key={`heatmap-rect-${bin.row}-${bin.column}`}
                                    className="visx-heatmap-rect"
                                    width={bin.width}
                                    height={bin.height}
                                    x={bin.y}
                                    y={bin.x}
                                    fill={bin.color}
                                    onClick={() => {
                                        if (!events) return;
                                        const { row, column } = bin;
                                        alert(JSON.stringify({ row, column, bin: bin.bin }));
                                    }}
                                />
                            )),
                        )
                    }
                </HeatmapRect>
        </svg>
    );
};

export default Example;
