//! MagicSpot 2's identities, kept distinct from Spotifast and MagicSpot v3.

pub const COMMAND: &str = "magicspot2";
pub const DISPLAY_NAME: &str = "MagicSpot";
pub const APP_ID: &str = "com.falleng101.magicspot2";
pub const REPOSITORY: &str = "FallenG101/MagicSpot2";

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn new_line_does_not_reuse_either_previous_app_identity() {
        assert_ne!(COMMAND, "spotifast");
        assert_ne!(COMMAND, "magicspot");
        assert_ne!(APP_ID, "rocks.spotifast.Spotifast");
        assert_ne!(APP_ID, "com.falleng101.magicspot");
        assert_eq!(REPOSITORY, "FallenG101/MagicSpot2");
    }
}
