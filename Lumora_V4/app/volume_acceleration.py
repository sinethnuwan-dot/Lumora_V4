class VolumeAcceleration:

    def calculate(
        self,
        previous_volume: float,
        current_volume: float,
        elapsed_seconds: float,
    ) -> float:

        if elapsed_seconds <= 0:
            return 0.0

        return (
            current_volume - previous_volume
        ) / elapsed_seconds


volume_acceleration = VolumeAcceleration()