{
  description = "Rotaboxes hacking server";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url     = "github:nixos/nixpkgs/nixos-23.05";

  outputs = {
    self,
    flake-utils,
    nixpkgs,
    ...
  }:
    flake-utils.lib.eachSystem
    [
      flake-utils.lib.system.x86_64-linux
    ]
    (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python310.withPackages (ps: with ps; [
          hid
          pynput
          websockets
        ]);
      in {
        devShells = {
          default = python.env;
        };
      }
    );
}
