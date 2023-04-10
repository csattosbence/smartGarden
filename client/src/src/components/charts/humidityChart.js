import {
    Area,
    AreaChart,
    XAxis,
    YAxis,
    CartesianGrid,
    ResponsiveContainer,
    Tooltip,
    Legend
  } from 'recharts';



const HumidityChart = ({data}) =>{
    return(
        <ResponsiveContainer width="80%" height={200}>
        <AreaChart  data={data}>
            <XAxis dataKey="currentDate"/>
            <YAxis dataKey="humidity"/>
            <Tooltip/>
            <Legend verticalAlign="top" height={36}/>
            <Area name="Humidity %" type="monotone" dataKey="humidity" stroke="#09b0e3" fill='#00d9d9'/>
        </AreaChart>
        </ResponsiveContainer>
    )
}

export default HumidityChart;