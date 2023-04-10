import {
    AreaChart,
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    ResponsiveContainer,
    Tooltip,
    Legend
  } from 'recharts';



const LightChart = ({data}) =>{
    return(
        <ResponsiveContainer width="80%" height={200}>
        <AreaChart  data={data}>
            <XAxis dataKey="currentDate"/>
            <YAxis dataKey="light"/>
            <Tooltip/>
            <Legend verticalAlign="top" height={36}/>
            <Area name="LUX" type="monotone" dataKey="light" stroke="#d9d200" fill='#fff700'/>
        </AreaChart>
        </ResponsiveContainer>
    )
}

export default LightChart;