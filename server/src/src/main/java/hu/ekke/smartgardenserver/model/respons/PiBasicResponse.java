package hu.ekke.smartgardenserver.model.respons;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.google.gson.annotations.SerializedName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


@Data
@AllArgsConstructor
@NoArgsConstructor
public class PiBasicResponse {
    @SerializedName("status_code")
    private String responseCode;

    private String description;
}
