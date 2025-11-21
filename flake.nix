{
  inputs = {
    flakelight-treefmt.url = "github:m15a/flakelight-treefmt";
    systems.url = "github:nix-systems/default";
  };

  outputs =
    {
      self,
      flakelight-treefmt,
      systems,
      ...
    }:
    flakelight-treefmt ./. {
      inputs.self = self;

      systems = import systems;

      devShell.packages =
        pkgs: with pkgs; [
          minio-client
          uv
        ];

      treefmtConfig = {
        programs = {
          ruff-format.enable = true;
          ruff-check.enable = true;
          nixfmt.enable = true;
          mdformat.enable = true;
          mdformat.plugins =
            ps: with ps; [
              mdformat-gfm
              mdformat-gfm-alerts
            ];
          yamlfmt.enable = true;
          dockerfmt.enable = true;
        };
      };
    };
}
