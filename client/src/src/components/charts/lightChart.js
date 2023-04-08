import {
    Line,
    LineChart,
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
            <LineChart data={data}>
                <XAxis dataKey="currentDate"/>
                <YAxis dataKey="light"/>
                <Tooltip/>
                <Legend verticalAlign="top" height={36}/>
                <Line name="LUX" type="monotone" dataKey="light" stroke="#e3dc09" />
                <CartesianGrid strokeDasharray="3 3" />
            </LineChart>
        </ResponsiveContainer>
    )
}

export default LightChart;