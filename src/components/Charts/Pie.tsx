import React from "react";
import { Pie } from "@visx/shape";
import { Group } from "@visx/group";
import { scaleOrdinal } from "@visx/scale";
import { LegendOrdinal } from '@visx/legend';

const colors = ['#26648E', '#4F8FC0', '#53D2DC']

type DataType = {key: string, value: number}[]

const ordinal = (data: DataType)=> scaleOrdinal({
  domain: data.map((d)=>d.key),
  range: colors,
});

const defaultMargin = { top: 20, right: 20, bottom: 20, left: 20 };

export type PieProps = {
    width: number,
    height: number,
    data: DataType
    margin?: typeof defaultMargin;
};

function MyPie({  width, height,
                                    data,
                                    margin = defaultMargin
                                }: PieProps) {
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;
    const radius = Math.min(innerWidth, innerHeight) / 2;
    const centerY = innerHeight / 2;
    const centerX = innerWidth / 2;
    const top = centerY + margin.top;
    const left = centerX + margin.left;
    const pieSortValues = (a: number, b: number) => b - a;
    const value = (d: {key: string, value: number}) => d.value;

    const getKeyValueColor = scaleOrdinal({
        domain: data.map((d) => d.key),
        range: colors,
    });


    return (
        <div style={{display: "flex", flexDirection:"column", alignItems:"center"}}>
                <svg width={width} height={height}>
                    <Group top={top} left={left}>
                        <Pie
                            data={data}
                            pieValue={value}
                            pieSortValues={pieSortValues}
                            outerRadius={radius}
                        >
                            {(pie) => {
                                return pie.arcs.map((arc, index) => {
                                    const {key, value} = arc.data;
                                    const [centroidX, centroidY] = pie.path.centroid(arc);
                                    const hasSpaceForLabel = arc.endAngle - arc.startAngle >= 0.1;
                                    const arcPath = pie.path(arc) || undefined;
                                    const arcFill = getKeyValueColor(key);
                                    return (
                                        <g key={`arc-${key}-${index}`}>
                                            <path d={arcPath} fill={arcFill}/>
                                            {hasSpaceForLabel && (
                                                <text
                                                    x={centroidX}
                                                    y={centroidY}
                                                    dy=".33em"
                                                    fill="#ffffff"
                                                    fontSize={15}
                                                    textAnchor="middle"
                                                    pointerEvents="none"
                                                >
                                                    {value}
                                                </text>
                                            )}
                                        </g>
                                    );
                                });
                            }}
                        </Pie>
                    </Group>
                </svg>
                <LegendOrdinal
                    scale={ordinal(data)}
                    direction="row"
                    itemDirection="row"
                    labelMargin="0 20px 0 20px"
                    shapeMargin="1px 0 0"
                />
            </div>
    );
}

const PieChart = ({data}: {data: DataType})=>{
   return <MyPie width={300} height={300} data={data}></MyPie>
}

export default PieChart