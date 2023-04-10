import {
    Line,
    LineChart,
    XAxis,
    YAxis,
    CartesianGrid,
    ResponsiveContainer,
    Tooltip,
    Legend,
    AreaChart,
    Area
  } from 'recharts';



const SoilMoistChart = ({data}) =>{
    return(
        <ResponsiveContainer width="80%" height={200}>
        <AreaChart  data={data}>
            <XAxis dataKey="currentDate"/>
            <YAxis dataKey="soilMoisture"/>
            <Tooltip/>
            <Legend verticalAlign="top" height={36}/>
            <Area name="Soilmoisture %" type="monotone" dataKey="soilMoisture" stroke="#018240" fill='#04db6c'/>
        </AreaChart>
        </ResponsiveContainer>
    )
}

export default SoilMoistChart;